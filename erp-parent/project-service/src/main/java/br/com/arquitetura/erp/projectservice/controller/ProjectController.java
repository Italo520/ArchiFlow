package br.com.arquitetura.erp.projectservice.controller;

import br.com.arquitetura.erp.projectservice.domain.Project;
import br.com.arquitetura.erp.projectservice.service.ProjectService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;



@RestController
@RequestMapping("/api/projects")
public class ProjectController {

    private final ProjectService projectService;


    @Autowired
    public ProjectController(ProjectService projectService) {
        this.projectService = projectService;
    }

    // GET /api/projects
    @GetMapping
    public List<Project> getAllProjects() {
        return projectService.findAllProjects();
    }

    // GET /api/projects/{id}
    @GetMapping("/{id}")
    public ResponseEntity<Project> getProjectById(@PathVariable Long id) {
        Optional<Project> project = projectService.findProjectById(id);
        return project.map(ResponseEntity::ok)
                      .orElseGet(() -> ResponseEntity.status(HttpStatus.NOT_FOUND).build());
    }

    // POST /api/projects
    @PostMapping
    public ResponseEntity<Project> createProject(@RequestBody Project project) {
        Project savedProject = projectService.saveProject(project);
        return new ResponseEntity<>(savedProject, HttpStatus.CREATED);
    }

    // PUT /api/projects/{id}
    @PutMapping("/{id}")
    public ResponseEntity<Project> updateProject(@PathVariable Long id, @RequestBody Project projectDetails) {
        Optional<Project> optionalProject = projectService.findProjectById(id);
        if (optionalProject.isPresent()) {
            Project existingProject = optionalProject.get();
            existingProject.setName(projectDetails.getName());
            existingProject.setDescription(projectDetails.getDescription());
            existingProject.setStartDate(projectDetails.getStartDate());
            existingProject.setEndDate(projectDetails.getEndDate());
            Project updatedProject = projectService.saveProject(existingProject);
            return ResponseEntity.ok(updatedProject);
        } else {
            return ResponseEntity.notFound().build();
        }
    }


    // DELETE /api/projects/{id}
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProject(@PathVariable Long id) {
        if (projectService.findProjectById(id).isPresent()) {
            projectService.deleteProject(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
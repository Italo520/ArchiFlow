package br.com.arquitetura.erp.projectservice.service;

import br.com.arquitetura.erp.projectservice.domain.Project;
import br.com.arquitetura.erp.projectservice.repository.ProjectRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;


@Service
public class ProjectService {

    private final ProjectRepository projectRepository;

    @Autowired
    public ProjectService( ProjectRepository projectRepository) {
        this.projectRepository = projectRepository;
    }


    @Transactional(readOnly = true)
    public List<Project> findAllProjects() {
        return projectRepository.findAll();
    }

    @Trasactional(readOnly = true)
    public Optional<Project> findProjectById(Long id) {
        if (projectRepository.existsById(id)) {
            return projectRepository.findById(id);
        } else {
            throw new IllegalArgumentException("Projeto com o id" + id + " não existe");
        }
    }

    @Transactional
    public Project saveProject(Project project) {
        return projectRepository.save(project);
    }

    @Transactional
    public void deleteProject(Long id) {
        if (projectRepository.existsById(id)) {
            projectRepository.deleteById(id);
        } else {
            throw new IllegalArgumentException("Projeto com o id" + id + " não existe");
        }

    }

}
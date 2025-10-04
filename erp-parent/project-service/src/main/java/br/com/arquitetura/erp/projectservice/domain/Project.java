import jackarta.persistence.*;
import java.time.LocalDate;
import Lombok.noargsconstructor;
import Lombok.Getter;
import Lombok.Setter;


@noargsconstructor
@Setter
@Getter
@Entity
@Table(name = "projects")
public class Project {
    @id
    @generatedvalue(strategy = GenerationType.IDENTITY)
    private Long id;

    @column(nullable = false)
    private String name;

    @column(columnDefinition = "TEXT")
    private String description;

    @column(name = "start_date")
    private LocalDate startDate;

    @column(name = "end_date")
    private LocalDate endDate;
}
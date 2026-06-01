# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8790?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8790
- Title: Next-Generation Geothermal Research and Development Act
- Congress: 119
- Bill type: HR
- Bill number: 8790
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-28T06:53:29Z
- Update date including text: 2026-05-28T06:53:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-13 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-13 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8790",
    "number": "8790",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Next-Generation Geothermal Research and Development Act",
    "type": "HR",
    "updateDate": "2026-05-28T06:53:29Z",
    "updateDateIncludingText": "2026-05-28T06:53:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2026-05-20T18:22:51Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-13T14:01:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-13T14:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "OR"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8790ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8790\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Mr. Harrigan (for himself and Ms. Salinas ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Energy Independence and Security Act of 2007 to direct research, development, demonstration, and commercial application activities in support of next-generation geothermal and closed-loop geothermal systems in various conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Next-Generation Geothermal Research and Development Act .\n#### 2. Geothermal energy\n##### (a) In general\nThe Energy Independence and Security Act of 2007 ( Public Law 110\u2013140 ) is amended\u2014\n**(1)**\nin section 612 ( 42 U.S.C. 17191 ; relating to definitions)\u2014\n**(A)**\nby redesignating paragraphs (1), (2), (3), (4), (5), (6), (7), and (8) as paragraphs (2), (3), (4), (5), (6), (7), (8), and (10), respectively;\n**(B)**\nby inserting before paragraph (2), as so redesignated, the following new paragraph:\n(1) Closed-loop geothermal systems The term closed-loop geothermal systems means a wellbore or subsurface circuit of wellbores containing a fluid heated through contact with the borehole wall. ;\n**(C)**\nby inserting after paragraph (8), as so redesignated, the following new paragraph:\n(9) Next-generation geothermal systems The term next-generation geothermal systems means\u2014 (A) enhanced geothermal systems; (B) closed-loop geothermal systems; (C) in supercritical conditions\u2014 (i) enhanced geothermal systems; or (ii) closed-loop geothermal systems; and (D) other innovative energy technologies. ; and\n**(D)**\nby adding at the end the following new paragraph:\n(11) Supercritical geothermal The term supercritical geothermal means energy derived from a subsurface rock resource in-situ existing at or above the supercritical conditions, whether relating to temperature or pressure, of the primary fluid present. ;\n**(2)**\nin section 613(b)(1) ( 42 U.S.C. 17192(b)(1) ; relating to hydrothermal research and development), by striking advanced geologic tools to assist and inserting advanced tools, including machine learning algorithms, to assist ;\n**(3)**\nin section 614 ( 42 U.S.C. 17193 ; relating to general geothermal systems research and development)\u2014\n**(A)**\nin subsection (d)(1), by striking among the Office of Fossil Energy, the Office of Energy Efficiency and Renewable Energy, and inserting across the Department ; and\n**(B)**\nin subsection (h)\u2014\n**(i)**\nin paragraph (1), by inserting and publicly available subsurface data, including data reported as part of fossil fuel and mining operations, after geothermal drilling information ; and\n**(ii)**\nin paragraph (2), by adding at the end the following new subparagraphs:\n(C) Updates The repository established under paragraph (1) shall be periodically updated in order to carry out the following: (i) Standardize data in a uniform manner to the maximum extent practicable and enable analysis across different projects. (ii) Enhance the accessibility and usability of data to increase analysis of geothermal energy and next-generation geothermal systems on regional, local, and site-specific scales. (iii) Increase uses of data, including data viewable by map and organization by common attributes, such as region. (iv) Make other improvements in functionality and usability, as determined by the Secretary. (D) Memorandum of understanding (i) In general The Secretary shall enter into a memorandum of understanding with the Secretary of the Interior, and with the heads of other relevant Federal departments, for notifying, sharing, and providing opportunities for additional data collection regarding shared geothermal development data from projects funded by the Department of the Interior and each such other relevant department, including data from mining, critical minerals, and energy projects, such as subsurface heat data, seismic data, lithology data, boundaries of State and federally protected areas, and existing transmission capacity. (ii) Prioritization To the maximum extent practicable, activities conducted pursuant to a memorandum of understanding under clause (i) shall prioritize heat, lithology, and strain profiles through deep exploration boreholes and control points for deep heat mapping and geothermal development. (E) Regional data probes The Secretary of the Interior may, in consultation with the Secretary, commission the drilling of supercritical geothermal exploration boreholes in representative geological provinces in the United States to provide control points for deep heat mapping and geothermal development. The resulting data shall include an exploration of heat, lithology, and strain profiles, and shall be shared publicly on the repository established under paragraph (1). (F) Study on site selection characteristics for supercritical geothermal The Secretary of the Interior shall, in consultation with the Secretary, conduct a study on site selection characteristics in representative geological provinces in the United States, including the United States territories of American Samoa, Guam, Northern Mariana Islands, Puerto Rico, and the U.S. Virgin Islands, for supercritical geothermal. ;\n**(4)**\nin section 615 ( 42 U.S.C. 17194 ; relating to enhanced geothermal systems research and development)\u2014\n**(A)**\nin the section heading, by striking Enhanced and inserting Next-generation ;\n**(B)**\nin subsection (a), by striking enhanced and inserting next-generation ;\n**(C)**\nin subsection (b)\u2014\n**(i)**\nin the heading, by inserting and closed-loop after Enhanced ;\n**(ii)**\nin the matter preceding paragraph (1), by inserting and closed-loop after enhanced ;\n**(iii)**\nin paragraph (11), by striking and after the semicolon;\n**(iv)**\nin paragraph (12), by striking the period and inserting ; and ; and\n**(v)**\nby adding at the end the following new paragraph:\n(13) the research topics specified in subparagraphs (1) through (12) in supercritical conditions. ;\n**(D)**\nin subsection (c)\u2014\n**(i)**\nby redesignating paragraph (7) as paragraph (8); and\n**(ii)**\nby inserting after paragraph (6) the following new paragraph:\n(7) Next-generation geothermal testing Not later than one year after the date of the enactment of this paragraph, the Secretary shall take such actions as may be necessary to ensure that at least one FORGE site has the capabilities to include next-generation geothermal testing, including, if practicable and technically feasible, closed-loop geothermal systems in supercritical conditions. ; and\n**(E)**\nby adding at the end the following new subsections:\n(e) Next-Generation geothermal research and development program (1) In general Within the Geothermal Technologies Office of the Department, the Secretary shall support a program of next-generation geothermal research, development, demonstration, and commercial application activities, including, if practicable and technically feasible, closed-loop geothermal systems in supercritical conditions. (2) Focus areas (A) In general The program described in paragraph (1) shall focus on the following topics: (i) Well completion. (ii) Permeability creation and management, including proppants and packers. (iii) Materials development and equipment design, including power production, specific to supercritical geothermal systems. (iv) Sensor development. (v) Water-rock geochemistry. (vi) Rock properties. (vii) Hard rock and deep drilling. (viii) Any other topics the Secretary determines necessary. (B) Prioritization In carrying out next-generation geothermal research under the program described in paragraph (1), the Secretary shall prioritize projects best able to produce iterative data for deep drilling projects in unique geodynamic settings on the following topics: (i) Characterization and crustal stress. (ii) Lab work. (iii) Drilling. (iv) Stimulation. (v) Power production. (C) Administration The Secretary may administer grants to institutions of higher education and private sector entities to carry out activities on the topics specified in subparagraph (A) and, to the maximum extent practicable, share data, results, and information publicly. (3) Report on water use Not later than five years after the date of the enactment of this subsection, the Secretary shall submit to the Committee on Natural Resources and the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report on the following: (A) Water use and estimated needs of enhanced geothermal systems. (B) Water use and estimated needs for closed-loop, and next-generation geothermal energy production. (C) The ability of next-generation geothermal systems to use brackish and nonpotable water. (D) The withdrawal and consumption of water per megawatt hour of next-generation geothermal systems, as compared to other power-generation technologies. (E) Technological and operational improvements that could lead to decreases in water withdrawal and consumption of next-generation geothermal systems. (4) Next-generation geothermal center of excellence (A) Establishment The Secretary shall award grants through a competitive, merit-reviewed process, to National Laboratories (as such term is defined in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 )), multi-institutional collaborations, public-private partnerships, or institutes of higher education (or consortia thereof) for the following: (i) The continuation and expansion of research, development, demonstration, testing, and commercial application activities applicable to FORGE sites, including activities in supercritical conditions. (ii) The establishment of a next-generation geothermal systems center of excellence. (B) Location In selecting National Laboratories, multi-institutional collaborations, public-private partnerships, or institutions of higher education (or a consortia thereof) for a center of excellence referred to in subparagraph (A), the Secretary shall consider the following criteria: (i) Whether the entity hosts an existing geothermal energy research and development program. (ii) Whether the entity has proven technical expertise to support geothermal energy research. (iii) Whether the entity has access to geothermal resources. (C) Purpose The center of excellence referred to in subparagraph (A) shall coordinate among existing FORGE sites, the Department, and National Laboratories to carry out the following: (i) Advance research, development, demonstration, and commercial application of next-generation geothermal energy technologies, including supercritical geothermal technologies, in response to industry and commercial needs, including by partnering with other academic or research institutions, industry, non-governmental organizations, and State, local, or Tribal governments. (ii) Foster collaboration for education, research, and partnership initiatives in order to support the technology, deployment, and workforce needs of the United States geothermal energy industry, including a focus on next-generation geothermal systems. (iii) Support workforce development across the next-generation geothermal systems energy development lifecycle. (iv) Provide educational, technical, and analytical assistance on next-generation geothermal systems to Federal agencies, industry, and State, local, and Tribal governments. (v) Collect and disseminate information on best practices in all areas relating to developing and managing geothermal energy resources and energy systems, including next-generation geothermal systems. (5) Commercial-readiness innovation grants (A) In general The Secretary shall award grants to accelerate the development, testing, and implementation of innovative technologies identified as areas for improving the performance of commercial geothermal energy projects using next-generation geothermal systems. (B) Focus areas Grants may be awarded under this paragraph for innovative technologies, including the following: (i) Hardrock drilling equipment, components, and systems, including bit design and vibration control. (ii) Reservoir characterization, well design and spacing, and completions. (iii) Data acquisition and analysis, including fiber optic sensing tools and methodologies. (C) Applications (i) In general An entity seeking a grant under this paragraph shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (ii) Prioritization In awarding grants under this paragraph, the Secretary shall give priority to the following: (I) Applicants, including for-profit entities and public-private partnerships, with demonstrated expertise relating to in-field development and commercial operations for geothermal energy projects. (II) Projects with the greatest ability to advance near-term commercial deployment of enhanced geothermal systems and closed-loop geothermal systems. (III) Projects that advance the commercialization of geothermal energy projects in diverse geological conditions or supercritical conditions. (D) Cost sharing The Federal share of the cost of a project carried out with a grant under this paragraph shall be not more than 80 percent. (f) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $150,000,000 for each of fiscal years 2027 through 2031. Such amounts shall be derived from amounts otherwise authorized to be appropriated to the Office of Energy Efficiency and Renewable Energy of the Department. ; and\n**(5)**\nin section 617 ( 42 U.S.C. 17196 ; relating to organization and administration of programs)\u2014\n**(A)**\nin subsection (e), by striking Committee on Science and Technology and inserting Committee on Science, Space, and Technology ; and\n**(B)**\nby amending subsection (f) to read as follows:\n(f) Progress reports Not later than one year after the date of the enactment of this subsection and every two years thereafter, the Secretary shall submit to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report that contains the following: (1) A description of the maximum potential of geothermal resources in the United States, including a consideration of next-generation geothermal systems. (2) Information relating to the results of projects undertaken under this section. (3) An assessment of the barriers to commercialization of next-generation geothermal technologies. (4) Such other information as the Secretary considers appropriate. .\n##### (b) Update to geothermal resource assessment\n**(1) In general**\nSection 2501 of the Energy Policy Act of 1992 ( 30 U.S.C. 1028 ) is amended\u2014\n**(A)**\nin subsection (c)\u2014\n**(i)**\nin the matter preceding paragraph (1), by inserting quadrennially before update ;\n**(ii)**\nin paragraph (1)(D)(ii), by striking and at the end;\n**(iii)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following new paragraph:\n(3) to the maximum extent practicable, by assessing regions of the United States, including the United States territories of American Samoa, Guam, Northern Mariana Islands, Puerto Rico, and the U.S. Virgin Islands, with significant potential for supercritical geothermal (as such term is defined in section 612 of the Energy Independence and Security Act of 2007 ( 42 U.S.C. 17191 )). ; and\n**(B)**\nby striking subsection (d).\n**(2) First update**\nThe first quadrennial update to the geothermal resource assessment carried out by the United States Geological Survey under subsection (c) of section 2501 of the Energy Policy Act of 1992, as amended by paragraph (1), shall be completed by not later than two years after the date of the enactment of this Act.\n##### (c) Clerical amendment\nThe table of contents in section 1(b) of the Energy Independence and Security Act of 2007 is amended by amending the item relating to section 615 to read as follows:\nSec. 615. Next-generation geothermal systems research and development. .",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8790ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Next-Generation Geothermal Research and Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-28T06:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Next-Generation Geothermal Research and Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-28T06:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Energy Independence and Security Act of 2007 to direct research, development, demonstration, and commercial application activities in support of next-generation geothermal and closed-loop geothermal systems in various conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-28T06:48:31Z"
    }
  ]
}
```

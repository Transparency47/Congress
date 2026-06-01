# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4903?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4903
- Title: Plastic Health Research Act
- Congress: 119
- Bill type: HR
- Bill number: 4903
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-03-19T08:07:18Z
- Update date including text: 2026-03-19T08:07:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4903",
    "number": "4903",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Plastic Health Research Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:18Z",
    "updateDateIncludingText": "2026-03-19T08:07:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
        "item": {
          "date": "2025-08-05T14:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "OK"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "LA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4903ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4903\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Ms. Stevens (for herself and Mr. Lucas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to carry out, expand, and coordinate programs relating to plastic exposure health research, to authorize grants, contracts, and agreements with respect to such research, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Plastic Health Research Act .\n#### 2. Plastic exposure health research\n##### (a) Expansion and coordination; research grants\nThe Public Health Service Act is amended by inserting after section 399V\u20137 ( 42 U.S.C. 280g\u201318 ) the following:\n399V\u20138. Plastic exposure health research (a) Expansion and coordination of research activities The Secretary, in consultation with the Administrator of the Environmental Protection Agency, the Commissioner of Food and Drugs, the Administrator of the National Oceanic and Atmospheric Administration, the Director of the National Institute of Standards and Technology, and the Director of the National Institute of Environmental Health Sciences, shall carry out, expand, and coordinate programs for the conduct and support of research with respect to understanding plastic exposures and the potential health effects stemming from plastic exposure. The Secretary shall prioritize such research that\u2014 (1) promotes the improvement of scientific quality through the development of vetted research methods that are reproducible, improve comparability of results among research studies, and develop standards definitions for microplastics and nanoplastics materials; (2) develops validated testing methodologies and reference materials for microplastics and nanoplastics in different media that are reproducible and improve comparability of results among research studies; or (3) fills gaps in the field of potential health effects research through the use of methods that improve the quality and comparability of scientific results. (b) Plastic exposure health research grants (1) In general The Secretary, in consultation with the Administrator of the Environmental Protection Agency, the Commissioner of Food and Drugs, the Administrator of the National Oceanic and Atmospheric Administration, the Director of the National Institute of Standards and Technology, and the Director of the National Institute of Environmental Health Sciences, may award grants or contracts to public entities, nonprofit entities, academic research institutions, or consortia of such entities (including such consortia that collaborate with private entities) to conduct scientific research on plastic exposure and the potential health effects stemming from such exposure. In awarding such grants and contracts, the Secretary shall prioritize research that\u2014 (A) improves the quality of scientific information through the development of vetted research methods that are reproducible, improve comparability of results among research studies, and develop standard definitions for microplastic and nanoplastic materials; (B) develops validated testing methodologies and reference materials for microplastics and nanoplastics in different media that are reproducible and improve comparability of results among research studies; or (C) fills gaps in the field of potential health effects research through the use of methods that improve the quality and comparability of scientific results. (2) Applications To be eligible for a grant or contract under this subsection, an entity shall submit to the Secretary an application in such form, in such manner, and containing such agreements, assurances, and information as the Secretary determines necessary. (3) Reports Not later than 1 year after the date of enactment of this section, and annually thereafter for each of the following 4 years, the Secretary shall submit to Congress, and make publicly available, a report that provides an overview of the research conducted or supported under this section, together with any relevant findings. (4) Information sharing The Secretary shall share the findings of the research supported by grants and contracts under this subsection with\u2014 (A) the heads of relevant institutes and agencies of the Department of Health and Human Services (including the Director of the National Institute of Environmental Health Sciences and the Commissioner of Food and Drugs); (B) the Administrator of the Environmental Protection Agency; (C) the Director of the National Institute of Standards and Technology; (D) the Administrator of the National Oceanic and Atmospheric Administration; and (E) the centers of excellence for plastic exposure health research described in section 463C. (5) Authorization of appropriations There is authorized to be appropriated to carry out this subsection $10,000,000 for each of fiscal years 2026 through 2030. (c) Plastic exposure defined In this section, the term plastic exposure means exposure to macroplastics, microplastics, and nanoplastics, including through plastic production and manufacturing, occupational exposure, environmental exposure, end-user interaction (such as handling and use of food packaging, manufactured goods, and textiles), plastic recycling, plastic degradation through natural or human-made processes, and plastic waste and disposal. .\n##### (b) Centers of excellence for plastic exposure health research\nThe Public Health Service Act is amended by inserting after section 463B ( 42 U.S.C. 285l\u20136 ) the following:\n463C. Centers of excellence for plastic exposure health research (a) In general The Secretary, acting through the Director of the Institute (in this section referred to as the Secretary ) may award grants to, or enter into appropriate funding agreements with, public entities, nonprofit entities, academic research institutions, or consortia of such entities (including such consortia that collaborate with private entities) to pay all or part of the cost of planning, establishing, or strengthening, and providing basic operating support for, centers of excellence to conduct and improve the quality of scientific research to inform public health determinations and increase public awareness (where scientifically warranted) with respect to the potential health effects caused by plastic exposure. Such centers shall prioritize research that\u2014 (1) develops standard material definitions; (2) improves the quality of scientific results to fill gaps in the field of research; (3) fills gaps in the field of health research through the use of methods that improve the quality and comparability of scientific results; or (4) develops vetted testing methodologies for microplastics and nanoplastics that can be replicated and can be compared to other testing methodologies. (b) Purposes of centers The purposes of the centers of excellence referred to in subsection (a) are\u2014 (1) to improve the quality of scientific results while researching the potential health effects stemming from plastic exposure, including identifying potential links between plastic exposure and such potential health effects; (2) to identify potential exposures to plastic and conduct hazard assessments and risk assessments; and (3) to increase public awareness (where scientifically warranted) of\u2014 (A) the potential health effects of plastic exposure, sources of such exposure, outcomes of hazard assessments, and the results of risk assessments relating to such exposure; and (B) the research referred to in\u2014 (i) paragraph (1); or (ii) section 399V\u20138(a). (c) Use of funds Funds made available under this section may be used for\u2014 (1) the development of plastic hazard, exposure, or risk assessment methodologies that can be replicated and compared to other methodologies, which shall include\u2014 (A) the comprehensive characterization and methods for characterization of the chemical and physical properties of microplastics, nanoplastics, macroplastics, and other plastics; (B) the development of validated testing methodologies for microplastics and nanoplastics in different media that can be replicated and compared to other testing methodologies; and (C) detailing the quality assurance and quality control measures taken to improve the scientific results; (2) the application of exposure methodologies (including both new and existing methodologies), if appropriately validated and controlled, to assess the potential burden of plastic exposures; (3) the support of research to assess potential health impacts of plastic exposure; and (4) increasing public awareness of research results, as scientifically warranted. (d) Policies A grant or agreement under this section shall be entered into in accordance with policies established by the Secretary. (e) Duration of grant or agreement A grant or agreement under this section shall be for a period of 5 years, and may be renewed by the Secretary for subsequent 5-year periods in the case of a center of excellence for which an appropriate technical and scientific peer review group established by the Secretary has\u2014 (1) reviewed the operations of such center; and (2) submitted to the Secretary a recommendation that such grant or agreement be renewed. (f) Coordination and information sharing with other institutes and agencies (1) Coordination The Secretary shall coordinate the activities under this section with related activities of other institutes and agencies of the Department of Health and Human Services (including the National Institute of Environmental Health Sciences and the Food and Drug Administration), the Environmental Protection Agency, the National Institute of Standards and Technology, and the National Oceanic and Atmospheric Administration. (2) Information sharing The Secretary shall share research findings of the centers of excellence referred to in subsection (a) with other institutes and agencies of the Department of Health and Human Services (including the National Institute of Environmental Health Sciences and the Food and Drug Administration), the Environmental Protection Agency, the National Institute of Standards and Technology, and the National Oceanic and Atmospheric Administration. (3) Reports Not later than 1 year after the date of enactment of this section, and annually thereafter for each of the following 4 years, the Secretary shall submit to Congress, and make publicly available, a report that provides an overview of the research conducted or supported under this section, together with any relevant findings. (g) Plastic exposure defined In this section, the term plastic exposure means exposure to macroplastics, microplastics, and nanoplastics, including through plastic production and manufacturing, occupational exposure, environmental exposure, end-user interaction (such as handling and use of food packaging, manufactured goods, and textiles), plastic recycling, plastic degradation through natural or human-made processes, and plastic waste and disposal. (h) Authorization of appropriations There is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-08-05",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-18T16:55:35Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4903ih.xml"
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
      "title": "Plastic Health Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Plastic Health Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to carry out, expand, and coordinate programs relating to plastic exposure health research, to authorize grants, contracts, and agreements with respect to such research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:35Z"
    }
  ]
}
```

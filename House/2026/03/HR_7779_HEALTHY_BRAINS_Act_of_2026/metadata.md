# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7779?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7779
- Title: HEALTHY BRAINS Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7779
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-05-14T08:07:42Z
- Update date including text: 2026-05-14T08:07:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7779",
    "number": "7779",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "HEALTHY BRAINS Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:42Z",
    "updateDateIncludingText": "2026-05-14T08:07:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:03:05Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "FL"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NM"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "VA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NE"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-28",
      "state": "PA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "OR"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "WA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7779ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7779\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Subramanyam (for himself and Mr. Bilirakis ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to require the Secretary of Health and Human Services to establish a program for the conduct and support of research, training, and health information dissemination with respect to environmental risk factors of neurodegenerative diseases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Harmonizing Environmental Analyses and Launching Therapeutic Hubs to Yield Bolstered Research And Innovation in Neurological Science Act of 2026 or the HEALTHY BRAINS Act of 2026 .\n#### 2. Research into environmental risk factors that may contribute to neurodegenerative disease\nPart B of title IV of the Public Health Service Act ( 42 U.S.C. 284 et seq. ) is amended by adding at the end the following:\n409K. Neurodegenerative disease environmental research (a) In general The Secretary shall establish a program for the conduct and support of research, training, and health information dissemination with respect to environmental risk factors (including environmental toxicant exposures) of neurodegenerative diseases. (b) Scope of research Research conducted or supported under this section shall\u2014 (1) be focused on\u2014 (A) potential environmental toxicants, including environmental stressors such as volatile organic compounds, particulate matter, per- and polyfluorinated substances, and heavy metals in environmental media such as air, water, food, and soil; (B) the mechanistic interactions of such toxicants with neurodegenerative disease outcomes; (C) the presymptomatic markers of neurodegenerative disease; and (D) advancing development of environmental health strategies to prevent, manage, treat, or slow the progression of neurodegenerative disease; and (2) may include research\u2014 (A) examining environmental exposures, including occupational risk factors, sociobehavioral factors, and social determinants of health; (B) using fundamental approaches to identify historical, existing, and emerging environmental risks and factors that affect disease progression; (C) examining multifactorial causation from chemical and nonchemical exposures; (D) examining prevalence of the disease in relation to the distribution of exposures across communities and populations; (E) examining the expression of disease traits that result from the interplay of genes and environment; and (F) exploring physiological mechanisms driving neurodegeneration from toxicant exposures. (c) Coordination within HHS (1) In general In carrying out the program under subsection (a), the Secretary shall\u2014 (A) provide for coordination across the programs and activities of the Department of Health and Human Services to avoid duplication; and (B) expand the funding of environmental health research by leading an ongoing, coordinated, and focused effort to fund new and existing centers for the study and evaluation of environmental risk factors (including environmental toxicants) of neurodegenerative diseases. (2) Biennial report In carrying out paragraph (1), the Secretary shall\u2014 (A) submit a biennial report detailing the findings and conclusions of research under this section to\u2014 (i) the Committees on Appropriations of the House of Representatives and the Senate; (ii) the Committee on Energy and Commerce of the House of Representatives; and (iii) the Committee on Health, Education, Labor, and Pensions of the Senate; (B) post each report under subparagraph (A) on the public website of the Department of Health and Human Services; and (C) include the information reported pursuant to subparagraph (A) in the triennial report under section 403. (d) Collaborative Centers for Neurodegenerative Disease Environmental Research (1) In general In carrying out the program under subsection (a), the Secretary shall provide for the establishment of research centers, to be known as Collaborative Centers for Neurodegenerative Disease Environmental Research (in this section each referred to as a Collaborative Center ) at institutions of higher education, medical centers, and other appropriate entities. (2) Requirements With respect to neurodegenerative disease, each Collaborative Center shall\u2014 (A) conduct and support basic, applied, and clinical research on the effects of environmental risk factors (including environmental toxicants), including with respect to disease progression; (B) use the facilities of a single institution or a consortium of cooperating institutions to administer the Collaborative Centers and meet such qualifications as may be prescribed by the Secretary; (C) be anchored in population-based, environmental health research; (D) conduct interdisciplinary and collaborative research that spans basic, applies, population-based, or clinical research; (E) coordinate with existing intramural and extramural efforts of the Department of Health and Human Services; and (F) collaborate with relevant partners and stakeholders, including researchers, health professionals, nonprofit organizations, patients, and caregivers, to understand the effects of environmental risk factors (including environmental toxicants) of neurodegenerative disease and progression thereof. (3) Discretionary activities With respect to neurodegenerative diseases, each Collaborative Center may\u2014 (A) provide career enhancement and training opportunities for scientists, researchers, environmental professionals, and health professionals, including through the provision of stipends; (B) conduct programs to provide information and continuing education to health professionals, including through the provision of stipends; (C) conduct programs for the dissemination of information to the public regarding research findings and proposed prevention strategies when appropriate; (D) separately or in collaboration with other Collaborative Centers or governmental agencies, establish a nationwide data system that\u2014 (i) includes data derived from comprehensive and representative patient populations with neurodegenerative diseases; and (ii) where possible, compares relevant data involving general populations; (E) separately or in collaboration with other Collaborative Centers, establish a clearinghouse, to be known as the Environmental Contributions to Neurodegenerative Disease Information Clearinghouse, to facilitate and enhance knowledge and understanding of environmental risk factors of neurodegenerative diseases; and (F) separately or in collaboration with other Collaborative Centers, establish a national education program that fosters a national focus on environmental risk factors of neurodegenerative diseases. (4) Duration of support The period of support for a Collaborative Center under this section shall not exceed 5 years, except that such period may be extended by the Secretary for one or more additional periods of not more than 5 years if\u2014 (A) the operations of such Collaborative Center have been reviewed by an appropriate technical and scientific peer review group established by the Secretary; and (B) such group has recommended to the Secretary that such period should be extended. (e) Authorization of appropriations To carry out this section, there is authorized to be appropriated $50,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-03-30T19:38:30Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7779ih.xml"
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
      "title": "HEALTHY BRAINS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEALTHY BRAINS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Harmonizing Environmental Analyses and Launching Therapeutic Hubs to Yield Bolstered Research And Innovation in Neurological Science Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to require the Secretary of Health and Human Services to establish a program for the conduct and support of research, training, and health information dissemination with respect to environmental risk factors of neurodegenerative diseases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T06:18:33Z"
    }
  ]
}
```

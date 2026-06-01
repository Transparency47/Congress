# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/598?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/598
- Title: Unearth Innovation Act
- Congress: 119
- Bill type: S
- Bill number: 598
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/598",
    "number": "598",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Unearth Innovation Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-13T20:29:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s598is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 598\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Hickenlooper (for himself and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo establish a mineral and mining innovation program within the Department of Energy to advance domestic mineral resources, economic growth, and national security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unearth Innovation Act .\n#### 2. Mineral and mining innovation initiative\n##### (a) Definitions\nIn this section:\n**(1) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(2) Initiative**\nThe term initiative means the mineral and mining innovation initiative established under subsection (b).\n**(3) Mining University**\nThe term mining university means an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) with a mining, metallurgical, geological, or mineral engineering program accredited by the Accreditation Board for Engineering and Technology, Inc.\n**(4) Secretary**\nThe term Secretary means the Secretary of Energy.\n##### (b) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish an initiative within the Department of Energy, the purposes of which are\u2014\n**(1)**\nto support the research, development, deployment, and commercialization of emerging technologies and practices suitable for responsibly identifying, characterizing, mining, extracting, processing, recycling, and reprocessing the minerals required across multiple industries in the United States to advance domestic mineral resources, circularity, economic growth, national security, and other goals, as determined by the Secretary;\n**(2)**\nto accelerate the research, development, and integration of advanced technologies, data analytics, responsible mining and mineral recovery practices, advanced techniques for separation or processing facilities to minimize human impacts, and extractive processes intended to minimize environmental impact, increase per-unit productivity, optimize resource utilization, and promote technology adaptation, community engagement, and social acceptance of mining; and\n**(3)**\nto coordinate with the National Institute of Occupational Safety and Health of the Centers for Disease Control and Prevention, the Office of Surface Mining Reclamation and Enforcement, and the Mine Safety and Health Administration of the Department of Labor on safety and mining innovation.\n##### (c) Duties\n**(1) In general**\nIn carrying out the initiative, the Secretary, in coordination with the Secretary of the Interior, shall identify, study, evaluate, test, and demonstrate hard rock mineral mining, unconventional mineral recovery, refining, and processing technologies and practices to improve\u2014\n**(A)**\nidentification of new potential domestic mineral resources and trends;\n**(B)**\ncharacterization and mapping of domestic mineral resources;\n**(C)**\nstatistical capabilities of the United States, with respect to domestic and global mineral resources;\n**(D)**\nenvironmental performance of mining and mineral recovery, including\u2014\n**(i)**\nreducing air emissions and improving water management;\n**(ii)**\nimproving energy efficiency; and\n**(iii)**\nminimizing tailings and other waste, mining footprint, and environmental impact;\n**(E)**\nefficiency and productivity of mining, including co-mineral and byproduct recovery, mineral processing, and resource utilization;\n**(F)**\ndata collection, analytics, and sharing;\n**(G)**\nmine safety;\n**(H)**\nmine reclamation, remediation, and reuse;\n**(I)**\ncommunity engagement, consultation with Indian Tribes, and social perception of mining;\n**(J)**\nemerging and new technologies for mineral recovery from unconventional sources;\n**(K)**\ntraining and education for the mining workforce; and\n**(L)**\nthe usable lifespan of products containing critical minerals through reuse, repurposing, and repairability.\n**(2) Research and development areas of focus**\nIn carrying out the initiative, the Secretary, in coordination with the Secretary of the Interior, shall focus research, development, deployment, and commercialization activities in areas related to\u2014\n**(A)**\nmineral exploration, discovery, and characterization science and technology, including\u2014\n**(i)**\ngeophysical surveys;\n**(ii)**\ngeochemical surveys;\n**(iii)**\nuncrewed survey platforms, including uncrewed aerial vehicles;\n**(iv)**\nproximal sensing, including automatic spectroscopic scanning of drilling cores;\n**(v)**\ncharacterizing mine waste, including mine-influenced water; and\n**(vi)**\nother advanced technologies;\n**(B)**\nmineral production and mine remediation and closure, including\u2014\n**(i)**\nadvanced drilling, sampling, and extraction technologies;\n**(ii)**\nmine design, including innovations that maximize resource use, environmental benefit, and end uses of land;\n**(iii)**\ndigital mining solutions;\n**(iv)**\nin-situ mineral recovery and other advanced extraction techniques;\n**(v)**\nprocessing techniques, including\u2014\n**(I)**\ngeometallurgy;\n**(II)**\nbeneficiation;\n**(III)**\nextraction from increasingly low-grade ores and deeper mines;\n**(IV)**\nco-mineral and byproduct recovery;\n**(V)**\nmultimineral refining;\n**(VI)**\nwhole rock processing; and\n**(VII)**\ngreenhouse gas reduction and sequestration; and\n**(vi)**\nremediation techniques, including\u2014\n**(I)**\nreclamation;\n**(II)**\ntailings and waste management; and\n**(III)**\nextraction and reprocessing of valued materials from waste on abandoned mine land and at active and inactive mine sites;\n**(C)**\ncritical mineral recycling technologies, including battery recycling;\n**(D)**\nsocial acceptance of mining and mineral processes, technologies, and projects, including\u2014\n**(i)**\nresearch to identify perspectives and priorities of communities local to prospective mining sites;\n**(ii)**\nresearch to identify strategies for community engagement and potential short-term and long-term benefits of mining for local communities;\n**(iii)**\nresearch to provide socially-informed technology research, design, and development priorities;\n**(iv)**\nbest practices for developing community benefit agreements and plans that address community priorities and mitigate potential environmental and economic harm that may result from mining; and\n**(v)**\nconsultation and engagement with Indian Tribes; and\n**(E)**\nother research areas, as determined by the Secretary, to support the program.\n**(3) Areas of focus for reevaluation**\nNot less frequently than once every 5 years, the Secretary, in carrying out the initiative in coordination with the Secretary of the Interior, shall consult with Indian Tribes, representatives from academic institutions (including mining universities), National Laboratories, and the mining industry\u2014\n**(A)**\nto reevaluate the status of, and opportunities for, mineral and mining research and development; and\n**(B)**\nto revise the list of areas described in paragraph (2)(E).\n##### (d) Coordination\nIn carrying out this section, the Secretary shall coordinate with the Secretary of the Interior through, at a minimum\u2014\n**(1)**\ninteragency activities associated with the research, development, deployment, and commercialization of hard rock mining and unconventional mineral recovery technologies;\n**(2)**\nleveraging existing mineral research within Federal agencies;\n**(3)**\nengagement with industry, academia, Indian Tribes, and nongovernmental entities to identify innovation gaps and opportunities related to minerals and mining;\n**(4)**\nalignment of applied academic and Federal mineral and mining research and development with economic, energy, and national security needs; and\n**(5)**\ncertification or validation of emerging technologies or best practices that demonstrate significant economic, environmental, and security benefits, including resource optimization, environmental sustainability, community engagement, and workforce development; and\n##### (e) Collaboration\n**(1) In general**\nIn carrying out this section, the Secretary and the Secretary of the Interior may enter into cooperative agreements, contracts, or other arrangements, including partnerships, with Indian Tribes and academic, public, private, and nongovernmental entities located in the United States, any territory or possession of the United States, or a country described in subparagraph (B) or (C) of section 12(3) of the Strategic and Critical Materials Stock Piling Act ( 50 U.S.C. 98h\u20133(3) ).\n**(2) Prioritization**\nIn carrying out paragraph (1), the Secretary and the Secretary of the Interior shall, to the maximum extent practicable, prioritize entering into cooperative agreements, contracts, or other arrangements with academic institutions, including mining universities.\n##### (f) Report\nNot later than 3 years after the date of enactment of this Act, the Secretary and the Secretary of the Interior shall submit to Congress a report describing the results of the duties carried out under subsection (c).\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $100,000,000 for each of fiscal years 2026 through 2035, to remain available until expended.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
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
        "name": "Energy",
        "updateDate": "2025-03-17T15:38:00Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s598is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Unearth Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T03:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unearth Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a mineral and mining innovation program within the Department of Energy to advance domestic mineral resources, economic growth, and national security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:28Z"
    }
  ]
}
```

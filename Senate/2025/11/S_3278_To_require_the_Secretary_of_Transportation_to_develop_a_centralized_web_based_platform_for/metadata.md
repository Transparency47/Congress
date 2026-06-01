# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3278?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3278
- Title: SMART Infrastructure Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3278
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-05T15:04:03Z
- Update date including text: 2026-01-05T15:04:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3278",
    "number": "3278",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "SMART Infrastructure Act of 2025",
    "type": "S",
    "updateDate": "2026-01-05T15:04:03Z",
    "updateDateIncludingText": "2026-01-05T15:04:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T21:00:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3278is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3278\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Ms. Lummis (for herself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Transportation to develop a centralized, web-based platform for managing, submitting, and tracking documents and processes relating to compliance with the National Environmental Policy Act of 1969, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Modeling for Advanced, Rapid Transportation Infrastructure Act of 2025 or the SMART Infrastructure Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nFederal permitting processes for infrastructure projects are often delayed due to inefficient coordination, imperfect communication of complex information, manual data handling, and lack of transparency;\n**(2)**\n2-dimensional paper- and PDF-based project designs impede the effective communication of complex, integrated engineering-based project information to government agencies, project stakeholders, laypersons, and local communities, causing delays in permitting and project delivery;\n**(3)**\ndigital twin technology enables real-time, high quality, high resolution, data-driven modeling of infrastructure projects that improves planning, environmental review, and stakeholder collaboration;\n**(4)**\ndigital twin technology is widely available on the commercial market from a variety of vendors;\n**(5)**\ndigital twins of infrastructure projects include and preserve detailed information about the project, acting as a single source of truth for all participants in the development of the project, which improves quality, reduces project risk, and accelerates delivery;\n**(6)**\ntechnological progress in the planning, permitting, design, construction, delivery, operation, and management of infrastructure is best achieved when design models are developed and transmitted in interoperable, digital, high-fidelity, 3-dimensional formats;\n**(7)**\nan electronic NEPA portal can centralize permitting data, streamline reviews, reduce environmental review timelines, and enhance public access to environmental documents; and\n**(8)**\nmodernizing permitting processes will accelerate critical infrastructure development, support economic growth, and ensure environmental protections.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Transportation and Infrastructure of the House of Representatives.\n**(2) Covered infrastructure project**\nThe term covered infrastructure project means any infrastructure project under Title 49 for which the Department of Transportation is the lead agency.\n**(3) Digital twin**\nThe term digital twin , with respect to an infrastructure project or infrastructure asset, means a high-fidelity, digital model of the infrastructure project or infrastructure asset that\u2014\n**(A)**\nintegrates real-time data from design, construction, operation, maintenance, and environmental factors to simulate the performance and impacts of the infrastructure project or infrastructure asset; and\n**(B)**\nis used to ensure greater accuracy, efficiency, and seamless integration of elements throughout the infrastructure project or infrastructure asset lifecycle.\n**(4) Eligible project**\nThe term eligible project means a covered infrastructure project for which each of the following are used:\n**(A)**\n1 or more digital twins.\n**(B)**\nThe e-NEPA portal developed under section 5(a).\n**(5) e-NEPA document**\nThe term e-NEPA document means an electronic environmental document or other NEPA-related document, including a permitting document, that is developed, submitted, reviewed, or tracked through the use of an e-NEPA portal.\n**(6) e-NEPA portal**\nThe term e-NEPA portal means a centralized, web-based platform\u2014\n**(A)**\nfor managing, submitting, and tracking documents and processes relating to NEPA compliance; and\n**(B)**\nthrough which e-NEPA documents are developed with interactive, digital technologies and systems to streamline\u2014\n**(i)**\ndocument development; and\n**(ii)**\ncommunications between project sponsors, government agencies, and community stakeholders with respect to the documents and processes required under NEPA.\n**(7) Environmental document**\nThe term environmental document has the meaning given the term in section 111 of NEPA ( 42 U.S.C. 4336e ).\n**(8) Infrastructure**\nThe term infrastructure means physical infrastructure.\n**(9) Lead agency**\nThe term lead agency has the meaning given the term in section 111 of NEPA ( 42 U.S.C. 4336e ).\n**(10) NEPA**\nThe term NEPA means the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n**(11) Open application programming interface**\nThe term open application programming interface mean an open source, machine-readable specification format that facilitates the integration of different systems from a variety of vendors, allowing the free exchange of data between engineering software tools, and enabling clear documentation and communication, without users needing access to the source code.\n**(12) Secretary**\nThe term Secretary means the Secretary of Transportation.\n#### 4. Digital twin implementation in permitting\n##### (a) Guidelines for adoption of digital twin technology\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Secretary, in coordination with the Council on Environmental Quality and relevant Federal agencies, shall establish guidelines for integrating digital twin technology into the permitting process for covered infrastructure projects.\n**(2) Requirements**\n**(A) In general**\nThe guidelines established under paragraph (1) shall include\u2014\n**(i)**\nstandards for creating and maintaining digital twins to model project impacts, including environmental, economic, and operational factors;\n**(ii)**\nrequirements for interoperability with existing Federal permitting systems; and\n**(iii)**\nprotocols for real-time data integration from environmental sensors, geographic information systems, and stakeholder inputs.\n**(B) Open application programming interfaces**\nThe standards described in subparagraph (A)(i) shall include recommendations that digital twins be developed with open application programming interfaces.\n##### (b) Pilot program\n**(1) In general**\nNot later than 120 days after the date of enactment of this Act, the Secretary shall establish a pilot program to test digital twin applications in not less than 10 covered infrastructure projects across diverse sectors.\n**(2) Requirements**\nThe pilot program established under paragraph (1) shall evaluate\u2014\n**(A)**\nthe extent of any\u2014\n**(i)**\nreductions in permitting timelines;\n**(ii)**\nimprovements in environmental impact assessments;\n**(iii)**\ncost savings; and\n**(iv)**\nstakeholder collaboration outcomes; and\n**(B)**\nthe importance of early public stakeholder engagement.\n**(3) Report**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall submit to the appropriate committees of Congress a report on the findings of the pilot program.\n#### 5. Establishment of e-NEPA portal\n##### (a) Development\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Secretary, in coordination with the Council on Environmental Quality, the Administrator of the Environmental Protection Agency, and the Secretary of Commerce, shall develop an e-NEPA portal for covered infrastructure projects.\n**(2) Requirements**\nThe e-NEPA portal developed under paragraph (1) shall\u2014\n**(A)**\nserve as a centralized platform for submitting, reviewing, and tracking e-NEPA documents;\n**(B)**\nintegrate with digital twin models to provide real-time visualization of the impacts of covered infrastructure projects;\n**(C)**\nprovide public access to\u2014\n**(i)**\nnonsensitive e-NEPA documents; and\n**(ii)**\ncomment periods; and\n**(D)**\ninclude secure data storage compliant with Federal cybersecurity standards.\n##### (b) Agency coordination\n**(1) Requirement**\nBeginning not later than January 1, 2028, all Federal agencies involved in an environmental review under NEPA for a covered infrastructure project shall use the e-NEPA portal developed under subsection (a) for all permitting relating to that covered infrastructure project.\n**(2) Role of the Secretary**\nFor each covered infrastructure project for which the e-NEPA portal developed under subsection (a) is used, the Secretary shall\u2014\n**(A)**\noversee portal-based coordination; and\n**(B)**\nensure compliance with statutory deadlines.\n##### (c) Public interface\nThe e-NEPA portal developed under subsection (a) shall include a public interface allowing stakeholders and members of the public, including communities\u2014\n**(1)**\nto access, for covered infrastructure projects\u2014\n**(A)**\nproject timelines;\n**(B)**\nnonsensitive e-NEPA documents; and\n**(C)**\ninformation relating to the status of permitting for the covered infrastructure project; and\n**(2)**\nto submit comments on a digital platform or website during NEPA public comment periods.\n#### 6. Accelerated permitting timelines\n##### (a) Streamlined Reviews\n**(1) In general**\nThe Secretary shall use all available existing authorities to reduce NEPA environmental review timelines for eligible projects by not less than 25 percent compared to existing averages.\n**(2) Implementation**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall promulgate guidance or regulations, as necessary, to implement the requirements of paragraph (1).\n##### (b) Interagency coordination\n**(1) In general**\nThe Secretary shall use the e-NEPA portal developed under section 5(a) to coordinate with other Federal, State, and local agencies to accelerate reviews for covered infrastructure projects.\n**(2) Single environmental document**\nA single environmental document shall be used across agencies for each covered infrastructure project.\n#### 7. Annual report\nThe Secretary shall submit to the appropriate committees of Congress an annual report that describes\u2014\n**(1)**\nany progress made with respect to\u2014\n**(A)**\nthe integration of digital twin technology into the permitting process for covered infrastructure projects; and\n**(B)**\nthe development and use of an e-NEPA portal for covered infrastructure projects;\n**(2)**\nany reductions in permitting timelines and costs for covered infrastructure projects; and\n**(3)**\nany environmental, public stakeholder, or community outcomes from the use of digital twins or the e-NEPA portal developed under section 5(a).",
      "versionDate": "2025-11-20",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-05T15:04:03Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3278is.xml"
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
      "title": "SMART Infrastructure Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SMART Infrastructure Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Streamlining Modeling for Advanced, Rapid Transportation Infrastructure Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Transportation to develop a centralized, web-based platform for managing, submitting, and tracking documents and processes relating to compliance with the National Environmental Policy Act of 1969, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:54Z"
    }
  ]
}
```

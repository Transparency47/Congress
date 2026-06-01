# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3376?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3376
- Title: Cargo Security Innovation Act
- Congress: 119
- Bill type: S
- Bill number: 3376
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T17:03:43Z
- Update date including text: 2026-01-07T17:03:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3376",
    "number": "3376",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Cargo Security Innovation Act",
    "type": "S",
    "updateDate": "2026-01-07T17:03:43Z",
    "updateDateIncludingText": "2026-01-07T17:03:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
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
        "item": [
          {
            "date": "2025-12-04T20:22:36Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-04T20:22:36Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MN"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3376is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3376\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mrs. Blackburn (for herself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Administrator of the Transportation Security Administration to establish a pilot project to evaluate the effectiveness of technologies to combat cargo theft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cargo Security Innovation Act .\n#### 2. Pilot project\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Transportation Security Administration.\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Transportation and Infrastructure of the House of Representatives.\n**(3) Eligible consortium**\nThe term eligible consortium means a consortium\u2014\n**(A)**\nconsisting of\u2014\n**(i)**\none or more private entities engaged in transportation (as that term is defined in section 13102 of title 49, United States Code), such as\u2014\n**(I)**\nowners or operators of an intermodal transportation hub or rail yard;\n**(II)**\nmotor carriers (as that term is defined in section 13102 of title 49, United States Code);\n**(III)**\nrail carriers (as that term is defined in section 10102 of title 49, United States Code);\n**(IV)**\nwater carriers (as that term is defined in section 13102 of title 49, United States Code); and\n**(V)**\nair carriers (as that term is defined in section 40102 of title 49, United States Code);\n**(ii)**\nrail police officers (within the meaning of section 28101 of title 49, United States Code), if applicable; and\n**(iii)**\nat least 1 State or local law enforcement entity; and\n**(B)**\nthat, in the determination of the Administrator\u2014\n**(i)**\nhas the resources and expertise necessary\u2014\n**(I)**\nto deploy advanced law enforcement or cargo security technologies at a pilot site; and\n**(II)**\nto evaluate the effectiveness of such a technology at combatting cargo theft; and\n**(ii)**\ndemonstrates capacity for interagency coordination and technology integration.\n**(4) Foreign entity of concern**\nThe term foreign entity of concern has the meaning given that term in section 40207 of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18741 ).\n**(5) Intermodal transportation hub**\nThe term intermodal transportation hub means an airport, land port, or seaport at which cargo can be transferred between different modes of transportation, including rail.\n**(6) Pilot project**\nThe term pilot project means the pilot project established under subsection (b).\n**(7) Pilot site**\nThe term pilot site means an intermodal transportation hub or rail yard designated as a pilot site under subsection (c).\n##### (b) Establishment\nThe Administrator, in consultation with the Secretary of Transportation, shall establish a pilot project to evaluate the effectiveness of advanced law enforcement and cargo security technologies at combatting cargo theft in transit and at and around intermodal transportation hubs and rail yards with elevated levels of cargo theft, including by providing grants to eligible consortia for the deployment and evaluation of those technologies.\n##### (c) Pilot sites\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Administrator shall designate up to 6 intermodal transportation hubs or rail yards as pilot sites for the deployment and evaluation of technologies under the pilot project.\n**(2) Pilot site diversity**\n**(A) In general**\nThe Administrator shall ensure geographic and operational diversity of pilot sites.\n**(B) Requirement**\nThe Administrator may designate not more than 1 pilot site in any 1 State.\n**(3) Prohibition on foreign technologies**\nIn carrying out the pilot project, the Administrator may not deploy at any pilot site technology produced by a foreign entity of concern.\n##### (d) Grants\n**(1) In general**\nIndividuals and entities associated with a pilot site may form an eligible consortium for purposes of pursuing a grant under the pilot project for such pilot site.\n**(2) Grant applications**\nAn eligible consortium desiring a grant under the pilot project shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require.\n**(3) Use of funds**\nAn eligible consortium may use a grant provided under the pilot project for\u2014\n**(A)**\ntechnology acquisition and deployment;\n**(B)**\npersonnel training and capacity building;\n**(C)**\ninteroperability with Federal data;\n**(D)**\noversight and technical evaluation; and\n**(E)**\nsuch other activities as the Administrator determines necessary.\n##### (e) Accountability\nAn eligible consortium that receives a grant under the pilot project shall maintain such records as the Administrator may require to facilitate an effective audit relating to the receipt of the grant, the use of grant amounts, or outsourcing activities.\n##### (f) Report\nNot later than 2 years after the date on which technology is first deployed at a pilot site under the pilot project, the Administrator shall submit to the appropriate committees of Congress a report that includes\u2014\n**(1)**\na description of the technologies deployed at each pilot site as of the date of submission of the report;\n**(2)**\nan evaluation of the effectiveness of those technologies in reducing cargo theft;\n**(3)**\na description of any outcomes or lessons learned from the deployment and evaluation of those technologies;\n**(4)**\na cost-benefit analysis for each of those technologies;\n**(5)**\ntechnology-related data generated under the pilot project in a machine-readable format; and\n**(6)**\nrecommendations for scaling or modifying the pilot project.\n##### (g) Sunset\nFor each pilot site, the pilot project shall terminate on the date that is 3 years after the initial deployment of technology at that pilot site under the pilot project.\n##### (h) GAO evaluation\nNot later than 1 year after the pilot project is terminated at all pilot sites pursuant to subsection (g), the Comptroller General of the United States shall submit to the appropriate committees of Congress a report evaluating the effectiveness of the pilot project.",
      "versionDate": "2025-12-04",
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
        "updateDate": "2026-01-07T17:03:42Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3376is.xml"
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
      "title": "Cargo Security Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cargo Security Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Transportation Security Administration to establish a pilot project to evaluate the effectiveness of technologies to combat cargo theft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:17Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6451?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6451
- Title: VA Transit Act
- Congress: 119
- Bill type: HR
- Bill number: 6451
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-02-03T09:05:49Z
- Update date including text: 2026-02-03T09:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6451",
    "number": "6451",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000560",
        "district": "2",
        "firstName": "Rick",
        "fullName": "Rep. Larsen, Rick [D-WA-2]",
        "lastName": "Larsen",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "VA Transit Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:49Z",
    "updateDateIncludingText": "2026-02-03T09:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:30:13Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6451ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6451\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Larsen of Washington introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to establish a pilot program for grants to improve access to public transportation services for veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Access to Transit Act or the VA Transit Act .\n#### 2. Pilot program for grants to improve public transportation services for veterans\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Transportation, in consultation with the Secretary of Veterans Affairs, shall establish a pilot program to award grants for the improvement of public transportation services for veterans.\n##### (b) Award of grants\n**(1) In general**\nIn carrying out the pilot program, the Secretary of Transportation may award grants to eligible recipients for eligible public transportation projects.\n**(2) Equitable distribution**\nThe Secretary of Transportation shall ensure that, to the extent practicable, grants awarded under this section are equitably distributed across geographic regions, including rural and Tribal communities.\n**(3) Grant recipient requirements**\nA grant under this section shall be subject to the requirements of\u2014\n**(A)**\nsection 5307 of title 49, United States Code, for eligible recipients of grants made in urbanized areas; and\n**(B)**\nsection 5311 of such title for eligible recipients of grants made in rural areas.\n**(4) Allocation to subrecipients**\nA recipient of a grant under this section may allocate amounts provided under the grant to a subrecipient.\n**(5) Locations**\nThe Secretary shall award grants under the pilot program to eligible recipients at not fewer than 5 eligible locations.\n##### (c) Grant application\nAn eligible recipient seeking the award of a grant under this section shall submit to the Secretary of Transportation an application in such form, in such manner, and containing such commitments and information as the Secretary considers necessary to carry out this section, including the following:\n**(1)**\nA description of the public transportation services that the eligible recipient intends to provide with such grant.\n**(2)**\nA list of all sites to be served by such services, including any sites that are facilities and organizations that serve veterans.\n**(3)**\nThe frequency and hours of operation of such services.\n**(4)**\nAn estimate of the number of veterans that would use such services.\n**(5)**\nEvidence that the eligible recipient has the legal, technical, and financial capacity to carry out the project proposed to be carried out with such grant.\n##### (d) Notification to veterans\nEach recipient awarded a grant under this section shall publicize and conduct outreach targeted to veterans regarding the transportation services funded under this section.\n##### (e) Termination\nThe pilot program established under this section shall terminate on the date that is 5 years after the date on which the pilot program commences.\n##### (f) Data collection\nNot later than 90 days after the termination date described in subsection (e), each recipient of a grant under this section shall submit to the Secretary of Transportation a report containing information on the projects carried out with such grant, including\u2014\n**(1)**\na description of the effects of expanded geographic coverage, improved service quality, increased frequency, or other activities funded with such grant on public transportation services for veterans;\n**(2)**\na description of any accessibility improvements made as a result of such projects;\n**(3)**\na description of changes in ridership due to such projects, including estimates or data regarding both general ridership and the number of veterans served;\n**(4)**\na description of the size and type of public transportation vehicles used in services funded with a grant awarded under this section;\n**(5)**\ninformation on whether the use of facilities or organizations that serve veterans has increased due to such projects; and\n**(6)**\nany other information the Secretary requires.\n##### (g) Report\nNot later than 180 days after the date on which the reports required under subsection (f) are submitted, the Secretary of Transportation shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate, a report on the results of the pilot program carried out under this section based on the information provided in the reports required under subsection (f).\n##### (h) Definitions\nIn this section, the following definitions shall apply:\n**(1) Eligible recipient**\nThe term eligible recipient means\u2014\n**(A)**\na State or local governmental entity; and\n**(B)**\na Tribe or Tribal governmental entity.\n**(2) Eligible location**\nThe term eligible location means\u2014\n**(A)**\na rural area, as defined in section 5302 of title 49, United States Code; or\n**(B)**\nan urbanized area, as defined in section 5302 of title 49, United States Code, that has a population of fewer than 200,000 individuals.\n**(3) Eligible transportation project**\nThe term eligible transportation project means\u2014\n**(A)**\na project planned, designed, and carried out to expand, modify, retain, or establish public transportation services that provide veterans access to locations of facilities or organizations that serve veterans that is\u2014\n**(i)**\na capital project; or\n**(ii)**\na project to acquire such public transportation services, including entering into service agreements with private providers of public transportation; or\n**(B)**\noperating costs associated with such project.\n**(4) Facility or organization that serves veterans**\nThe term facility or organization that serves veterans means\u2014\n**(A)**\na facility of the Department of Veterans Affairs;\n**(B)**\nan organization or facility that provides services to veterans using funds provided by the Department of Veterans Affairs; and\n**(C)**\nand organization or facility proven to serve a significant number or percentage of the local population of veterans.\n**(5) Net project cost**\nThe term net project cost has the meaning given such term in section 5302 of title 49, United States Code.\n**(6) Subrecipient**\nThe term subrecipient means a State or local governmental authority, a private nonprofit organization, or an operator of public transportation services.",
      "versionDate": "2025-12-04",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-22T16:18:28Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6451ih.xml"
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
      "title": "VA Transit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Transit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Access to Transit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish a pilot program for grants to improve access to public transportation services for veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:26Z"
    }
  ]
}
```

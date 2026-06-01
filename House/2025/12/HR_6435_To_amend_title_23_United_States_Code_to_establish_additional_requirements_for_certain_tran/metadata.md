# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6435
- Title: Transportation Megaprojects Accountability and Oversight Act
- Congress: 119
- Bill type: HR
- Bill number: 6435
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-02-03T09:05:40Z
- Update date including text: 2026-02-03T09:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6435",
    "number": "6435",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000623",
        "district": "10",
        "firstName": "Mark",
        "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
        "lastName": "DeSaulnier",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Transportation Megaprojects Accountability and Oversight Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:40Z",
    "updateDateIncludingText": "2026-02-03T09:05:40Z"
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
          "date": "2025-12-04T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:29:47Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6435ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6435\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. DeSaulnier (for himself and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to establish additional requirements for certain transportation projects with estimated costs of $2,500,000,000 or more, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transportation Megaprojects Accountability and Oversight Act .\n#### 2. Additional requirements for certain transportation projects\n##### (a) In general\nSection 106 of title 23, United States Code, is amended by adding at the end the following:\n(k) Megaprojects (1) Megaproject defined In this subsection, the term megaproject means a project that has an estimated total cost of $2,500,000,000 or more, and such other projects as may be identified by the Secretary. (2) Comprehensive risk management plan A recipient of Federal financial assistance under this title for a megaproject shall, in order to be authorized for construction, submit to the Secretary a comprehensive risk management plan that contains\u2014 (A) a description of the process by which the recipient will identify, quantify, and monitor the risks that might result in cost overruns, project delays, reduced construction quality, or reductions in benefits with respect to the megaproject; (B) examples of mechanisms the recipient will use to track risks identified pursuant to subparagraph (A); (C) a plan to control such risks; and (D) such assurances as the Secretary considers appropriate that the recipient will, with respect to the megaproject\u2014 (i) regularly submit to the Secretary updated cost estimates; and (ii) maintain and regularly reassess financial reserves for addressing known and unknown risks. (3) Peer review group (A) In general A recipient of Federal financial assistance under this title for a megaproject shall, not later than 90 days after the date when such megaproject is authorized for construction, establish a peer review group for such megaproject that consists of at least 5 individuals (including at least 1 individual with project management experience) to give expert advice on the scientific, technical, and project management aspects of the megaproject. (B) Membership (i) In general Not later than 180 days after the date of enactment of this subsection, the Secretary shall establish guidelines describing how a recipient described in subparagraph (A) shall\u2014 (I) recruit and select members for a peer review group established under such subparagraph; and (II) make publicly available the criteria for such selection and the identity of members so selected. (ii) Conflict of interest No member of a peer review group for a megaproject may have a direct or indirect financial interest in such megaproject. (C) Tasks A peer review group established under subparagraph (A) by a recipient of Federal financial assistance for a megaproject shall\u2014 (i) meet annually until completion of the megaproject; (ii) not later than 90 days after the date of the establishment of the peer review group and not later than 90 days after the date of any significant change, as determined by the Secretary, to the scope, schedule, or budget of the megaproject, review the scope, schedule, and budget of the megaproject, including planning, engineering, financing, and any other elements determined appropriate by the Secretary; and (iii) submit a report on the findings of each review under clause (ii) to the Secretary, Congress, and the recipient. (4) Transparency A recipient of Federal financial assistance under this title for a megaproject shall publish on the internet website of such recipient\u2014 (A) the name, license number, and license type of each engineer supervising an aspect of the megaproject; and (B) the report submitted under paragraph (3)(C)(iii), not later than 90 days after such submission. (5) Committee (A) In general Not later than 180 days after the date of enactment of this subsection, the Secretary of Transportation shall make appropriate arrangements with the Transportation Research Board (hereinafter referred to as the Board ) of the National Academies under which the Board shall convene a transportation megaprojects committee. (B) Duties The transportation megaprojects committee convened pursuant to subparagraph (A) shall\u2014 (i) perform a literature search and assessment of existing megaproject studies; (ii) review any relevant foreign experience and actions taken, with a particular focus on the United Kingdom and France; (iii) identify recurring or typical problems with megaprojects; (iv) outline possible approaches to dealing with the problems in the Federal and State context; and (v) recommend any changes in the Department of Transportation\u2019s approach to megaproject funding and oversight, such as a recommendation that each project be required to identify a peer group to work with project management and report to the Inspector General and Congress. (C) Report Not later than 3 years after the date of enactment of this subsection, the committee convened pursuant to subparagraph (A) shall submit to the Secretary, the Committee on Transportation and Infrastructure of the House of Representatives, and the Committee on Environment and Public Works of the Senate a report containing any results, findings, and recommendations made by the committee under subparagraph (B). .\n##### (b) Applicability\nThe amendment made by subsection (a) applies with respect to projects that are authorized for construction on or after the date that is 1 year after the date of enactment of this Act.",
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
        "updateDate": "2026-01-05T16:41:56Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6435ih.xml"
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
      "title": "Transportation Megaprojects Accountability and Oversight Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transportation Megaprojects Accountability and Oversight Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to establish additional requirements for certain transportation projects with estimated costs of $2,500,000,000 or more, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T08:18:27Z"
    }
  ]
}
```

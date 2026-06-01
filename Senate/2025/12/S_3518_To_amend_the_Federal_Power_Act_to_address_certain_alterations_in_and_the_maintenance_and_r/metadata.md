# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3518?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3518
- Title: FLOWS Act
- Congress: 119
- Bill type: S
- Bill number: 3518
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3518",
    "number": "3518",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "FLOWS Act",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T17:58:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:12Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "ME"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3518is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3518\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Ms. Murkowski (for herself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Power Act to address certain alterations in, and the maintenance and repair of, project works, to provide for the licensing of micro hydrokinetic energy projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Licensing for Operations of Water Structures Act or the FLOWS Act .\n#### 2. Hydropower maintenance and temporary adjustments\n##### (a) Alterations in project works\nSection 10(b) of the Federal Power Act ( 16 U.S.C. 803(b) ) is amended by adding at the end the following: Notwithstanding any other requirement of this part, the licensee shall not be required to obtain approval from the Commission for any nonsubstantial alteration or addition to project works under the plans approved by the Commission under section 9(a)(1). .\n##### (b) Maintenance and repair of project works\nSection 10(c) of the Federal Power Act ( 16 U.S.C. 803(c) ) is amended by adding at the end the following: Notwithstanding any other requirement of this part, the licensee shall not be required to obtain approval from the Commission for any routine maintenance, repair, or replacement of any portion of a project works necessary to maintain the project works in accordance with this subsection or for any seasonal or temporary adjustments to project operations in response to circumstances beyond the reasonable control of the licensee. .\n##### (c) Savings clause\nNothing in this section or an amendment made by this section\u2014\n**(1)**\naffects any authority of the Federal Energy Regulatory Commission\u2014\n**(A)**\nto require notice from a licensee under subsection (a) or (b) of section 10 of the Federal Power Act ( 16 U.S.C. 803 ); or\n**(B)**\nto enforce requirements of that section or the terms of a license issued under part I of the Federal Power Act ( 16 U.S.C. 792 et seq. ) with respect to the safety of any dam and appurtenant works and structures; or\n**(2)**\n**(A)**\nprecludes any prompt, informal consultation between the licensee and the Federal Energy Regulatory Commission, at the request of the licensee or the Federal Energy Regulatory Commission, with respect to the safety of any dam and appurtenant works and structures in advance of work to be undertaken under section 10 of the Federal Power Act ( 16 U.S.C. 803 ); or\n**(B)**\naffects any authority of the Federal Energy Regulatory Commission to require changes in advance of the work described in subparagraph (A) to protect the safety of any dam and appurtenant works and structures.\n#### 3. Micro hydrokinetic energy projects\nPart I of the Federal Power Act ( 16 U.S.C. 792 et seq. ) is amended by adding at the end the following:\n37. Licensing of micro hydrokinetic energy projects (a) Definition of micro hydrokinetic energy project In this section, the term micro hydrokinetic energy project \u2014 (1) means a project that\u2014 (A) has or will have an installed capacity of not more than 5 megawatts; and (B) converts to electric energy the hydrokinetic energy from a generator driven by a turbine from\u2014 (i) waves, tides, or currents in oceans, estuaries, or tidal areas; or (ii) free flowing water in rivers, lakes, streams, or man-made channels; and (2) does not include a project that impounds water to generate electricity. (b) Authorization The Commission may issue a license in accordance with this section for a term of not less than 10, and not more than 20, years for the construction, operation, and maintenance of project works for a micro hydrokinetic energy project. (c) Expedited licensing process (1) Notification of intent (A) Filing of notification An applicant for a license under this section shall commence the licensing process by filing a notification of intent with the Commission. (B) Existing license deadline Notwithstanding section 15(b)(1), an applicant for a license under this section shall file a notification of intent under subparagraph (A) not later than 2 years before the expiration of an existing license, if applicable. (2) Filing of application (A) In general Except as provided in subparagraph (B), an applicant for a license under this section shall submit to the Commission an application not later than 1 year after the date on which the applicant files a notification of intent under paragraph (1). (B) Existing license deadline Notwithstanding section 15(c)(1), an applicant for a license under this section shall file an application with the Commission not later than 1 year before the date of expiration of the term of an existing license, if applicable. (3) Deadline for issuance The Commission shall take final action on an application for a license under this section not later than 1 year after the date on which the application is filed under paragraph (2). (4) Schedule for final action To the extent reasonably practicable, the Commission and any applicable conditioning or permitting agencies shall establish, with respect to each micro hydrokinetic energy project that is the subject of a notification of intent to apply for a license under this section, a joint schedule that permits the timely completion of decisions required to be made with respect to, and the timely issuance of, authorizations required under Federal law by the Commission and the conditioning or permitting agencies, subject to the requirement that any joint schedule established under this paragraph shall comply with the deadline for final action established under paragraph (3). (d) Regulations (1) In general Not later than 180 days after the date of enactment of this section, the Commission shall promulgate regulations to implement this section in a manner that expedites the deployment of micro hydrokinetic energy projects while ensuring the safe operation of the micro hydrokinetic energy project in compliance with applicable Federal and State laws. (2) Inclusion The regulations promulgated under paragraph (1) shall provide for the use of 1 or more categorical exclusions, including allowing for extraordinary circumstances under which the categorical exclusion shall not be available, under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) for low disturbance activities necessary for micro hydrokinetic energy projects. (e) Report to congress The Commission shall submit to Congress a report describing the impacts of the micro hydrokinetic energy projects licensed under this section on the environment, the economy, and the reliability and affordability of electricity not later than the earlier of\u2014 (1) the date that is 5 years after the date of enactment of this section; and (2) the date on which the first 50 micro hydrokinetic energy projects licensed under this section have been operational for not less than 1 year. (f) Savings clause Nothing in this section affects any authority of the Commission, at the election of an applicant, to license the construction, operation, and maintenance of project works for a micro hydrokinetic energy project under any other provision of this part. .",
      "versionDate": "2025-12-17",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2026-04-02T13:43:26Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-04-02T14:06:59Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-04-02T14:05:05Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-04-02T14:28:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-01-12T16:38:37Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3518is.xml"
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
      "title": "FLOWS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FLOWS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Licensing for Operations of Water Structures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Power Act to address certain alterations in, and the maintenance and repair of, project works, to provide for the licensing of micro hydrokinetic energy projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:03:22Z"
    }
  ]
}
```

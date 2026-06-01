# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6357
- Title: TVA IRP Act
- Congress: 119
- Bill type: HR
- Bill number: 6357
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2026-02-03T09:05:41Z
- Update date including text: 2026-02-03T09:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6357",
    "number": "6357",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "TVA IRP Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:41Z",
    "updateDateIncludingText": "2026-02-03T09:05:41Z"
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
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:27:18Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6357ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6357\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Cohen (for himself and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Tennessee Valley Authority Act to provide for further transparency of the Tennessee Valley Authority, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TVA Increase Rate of Participation Act or the TVA IRP Act .\n#### 2. Office of Public Participation\nThe Tennessee Valley Authority Act of 1933 ( 16 U.S.C. 831k\u20131 ) is amended by inserting after section 12a the following:\n12b. Office of Public Participation (a) Establishment There is established in the Corporation an Office of Public Participation to engage with the public through direct outreach and education to facilitate greater understanding of the processes of the Authority and solicit broader participation in matters of the Authority affecting the public. (b) Hiring Hiring authority for the Office of Public Participation shall lay with the Board and such authority may not be delegated to Corporation staff. (c) Duties The Office of Public Participation established under subsection (a) shall\u2014 (1) act as a liaison to members of the public affected by and interested in Corporation proceedings, by providing ongoing process information on individual proceedings and responding to requests for technical assistance; (2) coordinate with other program offices of the Corporation to improve, or, as appropriate, make recommendations to improve processes in a manner responsive to public input, with the goal of ensuring processes are inclusive, fair, and easy to navigate; and (3) with public participation and feedback, create and facilitate a process not later than 1 year after the date of enactment of this section, for meaningful and open public engagement in the Authority\u2019s integrated resource planning process, including opportunities for intervention, discovery, filed comments or testimony, and an evidentiary hearing. (d) Public participation in integrated resource planning process The process required under subsection (b)(3) shall include\u2014 (1) a public comment period that begins not later than 100 days before release of a draft of an integrated resource plan and ends on the last day of the evidentiary hearing for such plan; and (2) a requirement for a response to any request for discovery from an intervenor not later than 15 days after such request is submitted. .\n#### 3. Integrated Resource Plan\n##### (a) In general\nIn drafting an integrated resource plan pursuant to section 113 of the Energy Policy Act of 1992 ( 16 U.S.C. 831m\u20131 ), the Board of Directors of the Tennessee Valley Authority shall\u2014\n**(1)**\noversee the process for meaningful and open public engagement in the integrated resource planning process established under section 12b of the Tennessee Valley Authority Act of 1933 (as added by this Act), including presiding over any evidentiary hearing required under such process;\n**(2)**\ninclude in such plan\u2014\n**(A)**\na long-term forecast of the Authority\u2019s sales and peak demand under various reasonable scenarios;\n**(B)**\na summary of electrical transmission investments planned by the Authority;\n**(C)**\nresource portfolios developed with the purpose of fairly evaluating the range of demand-side and supply-side technologies and services available to meet the Authority\u2019s service obligations; and\n**(D)**\nsensitivity analysis related to fuel costs, environmental regulations, electrification, distributed energy resources, and other uncertainties or risks;\n**(3)**\nnot later than 100 days before the public release of a draft of the plan, provide to the public the modeling assumptions used in developing such a plan, including costs and constraints on the model;\n**(4)**\nprovide in such draft plan details of how and where public input informed the plan;\n**(5)**\nevaluate whether the draft plan takes into account the features required under section 113(b)(2) of the Energy Policy Act of 1992 ( 16 U.S.C. 831m\u20131 ); and\n**(6)**\nissue a decision to approve, deny, or require modifications to such draft plan as necessary based on the evaluation under paragraph (5) and public input provided through the public comment period and evidentiary hearing required under section 12b of the Tennessee Valley Authority Act of 1933 (as added by this Act).\n##### (b) Tennessee Valley Authority least-Cost planning program\nSection 113(b)(2)(A) of the Energy Policy Act of 1992 ( 16 U.S.C. 831m\u20131 ) is amended by inserting resilience, extreme weather risk, impacts to public health, after dispatchability .",
      "versionDate": "2025-12-02",
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
        "name": "Energy",
        "updateDate": "2025-12-18T15:31:01Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6357ih.xml"
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
      "title": "TVA IRP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TVA IRP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TVA Increase Rate of Participation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Tennessee Valley Authority Act to provide for further transparency of the Tennessee Valley Authority, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:27Z"
    }
  ]
}
```

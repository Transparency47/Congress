# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6526
- Title: Clarity on Care Options Act
- Congress: 119
- Bill type: HR
- Bill number: 6526
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-05-11T14:06:46Z
- Update date including text: 2026-05-11T14:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Referred to the Subcommittee on Health.
- 2026-01-13 - Committee: Subcommittee Hearings Held
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Referred to the Subcommittee on Health.
- 2026-01-13 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6526",
    "number": "6526",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Clarity on Care Options Act",
    "type": "HR",
    "updateDate": "2026-05-11T14:06:46Z",
    "updateDateIncludingText": "2026-05-11T14:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-01-13T17:15:55Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-10T14:06:43Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6526ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6526\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mrs. Kiggans of Virginia introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to establish and maintain a publicly available directory of health care providers that accept assignments under the CHAMPVA program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clarity on Care Options Act .\n#### 2. Publicly available directory of health care providers that accept assignments under the CHAMPVA program\n##### (a) Annual query\nThe Secretary of Veterans Affairs shall require each entity that administers a network of health care providers under section 1703 of title 38, United States Code, to, on an annual basis\u2014\n**(1)**\nquery each provider in such network to determine whether the provider accepts assignments under the CHAMPVA program; and\n**(2)**\nsubmit the results of such queries to the Secretary.\n##### (b) Directory\nUtilizing the information submitted under subsection (a) and any other information available to the Secretary, the Secretary shall establish and maintain a publicly available directory of providers in such networks that accept assignments under the CHAMPVA program.\n##### (c) Implementation\n**(1) Annual queries**\nThe first queries required by subsection (a) shall be completed, and the results submitted to the Secretary, not later than 90 days after the date of the enactment of this Act.\n**(2) List of providers**\nThe first directory of providers required by subsection (b) shall be made publicly available not later than 180 days after the date of the enactment of this Act.\n##### (d) Annual report\nNot later than one year after the date of the enactment of this Act, and annually thereafter for four additional years, the Secretary shall submit to Congress a report on the extent to which the providers in such networks accept assignments under the CHAMPVA program. The report shall include the following information, broken down by State (as defined in section 101 of title 38, United States Code) and by Veterans Integrated Service Network:\n**(1)**\nThe number of providers in such networks that accept assignments under the CHAMPVA program.\n**(2)**\nThe percentage of providers in such networks that accept assignments under the CHAMPVA program and the percentage of providers in such networks that do not accept such assignments.\n**(3)**\nThe specific geographical areas that contain CHAMPVA program beneficiaries but do not contain providers that accept assignments under the CHAMPVA program.\n##### (e) Definitions\nIn this section:\n**(1)**\nThe term accept assignment , with respect to the CHAMPVA program, means to accept responsibility for the care of a CHAMPVA program beneficiary and thereby agree to accept the amount determined allowable under the CHAMPVA program as full payment for services and supplies rendered to the beneficiary.\n**(2)**\nThe term CHAMPVA program means the Civilian Health and Medical Program of the Department of Veterans Affairs under section 1781 of title 38, United States Code, and Part 17 of title 38, Code of Federal Regulations.",
      "versionDate": "2025-12-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-11T14:06:45Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2026-05-11T14:01:09Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-05-11T13:58:13Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-05-11T14:01:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-10T21:55:50Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6526ih.xml"
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
      "title": "Clarity on Care Options Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clarity on Care Options Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-10T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the Secretary of Veterans Affairs to establish and maintain a publicly available directory of health care providers that accept assignments under the CHAMPVA program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-10T09:48:20Z"
    }
  ]
}
```

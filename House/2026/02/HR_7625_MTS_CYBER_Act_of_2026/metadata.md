# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7625
- Title: MTS CYBER Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7625
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-05-16T08:07:38Z
- Update date including text: 2026-05-16T08:07:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-23 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-23 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7625",
    "number": "7625",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001240",
        "district": "6",
        "firstName": "Addison",
        "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
        "lastName": "McDowell",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "MTS CYBER Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:38Z",
    "updateDateIncludingText": "2026-05-16T08:07:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-23",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:34:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-23T20:55:41Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-20T16:33:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7625ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7625\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. McDowell introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Comptroller General of the United States to conduct a review of the budget, resources, and capabilities of the Coast Guard as the co-Sector Risk Management Agency for the marine transportation system.\n#### 1. Short title\nThis Act may be cited as the Marine Transportation System Cybersecurity Budget and Evaluation Report Act of 2026 or the MTS CYBER Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMaritime trade is essential to America\u2019s economic stability, supporting $2,100,000,000,000 in economic activity, or 41.5 percent of the global trade value of the United States.\n**(2)**\nThe increasing frequency and severity of cyber threats to the marine transportation system (hereinafter referred to as MTS ) presents economic and national security risks.\n**(3)**\nThe Department of Homeland Security and the Department of Transportation are designated as co-Sector Risk Management Agencies (hereinafter referred to as SRMAs ) for the MTS under Presidential Policy Directive 21, with further delegation of responsibilities to agencies such as the Coast Guard and the Transportation Security Administration as outlined in implementing documents.\n**(4)**\nExecutive Order 14116, issued by President Biden in February 2024, expands the United States Coast Guard\u2019s regulatory authorities to strengthen MTS cybersecurity.\n**(5)**\nThe Coast Guard issued a final cybersecurity rule, Cybersecurity in the Marine Transportation System , establishing mandatory incident reporting for regulated entities, significantly expanding the Coast Guard\u2019s cybersecurity oversight responsibilities.\n**(6)**\nThrough the Investing in America Agenda, the Biden administration dedicated $20,000,000,000 for United States port infrastructure, but it fails to specify cybersecurity-specific spending allocations to provide the Coast Guard with adequate resources and funding.\n**(7)**\nThe Coast Guard remains underfunded and understaffed for the purpose of sector risk management.\n**(8)**\nThe ability of the Coast Guard to fulfill SRMA duties is contingent upon adequate budgetary resources and a healthy workforce.\n**(9)**\nA Government Accountability Office audit is necessary to assess the budget and capabilities of the Coast Guard as an SRMA to ensure it can fulfill responsibilities for protecting the MTS against cyber threats.\n#### 3. Coast Guard Sector Risk Management Agency budget and capabilities review\n##### (a) GAO review\nNot later than 270 days after the date of enactment of this Act, the Comptroller General of the United States shall conduct a review to assess the funding and resource needs of the Coast Guard to fulfill the SRMA responsibilities of the Coast Guard, including\u2014\n**(1)**\nan evaluation of the sufficiency of Coast Guard funding for the sector risk management responsibilities, including funding for cybersecurity personnel, training, and enforcement, in light of statutory requirements under section 9002 of the National Defense Authorization Act for Fiscal Year 2021 and additional requirements in Presidential Policy Directive 21;\n**(2)**\nthe ability of Coast Guard personnel to evaluate compliance with cybersecurity requirements for regulated entities; and\n**(3)**\nthe sufficiency of guidance provided to industry stakeholders on implementing and complying with cyber regulations, assessed against applicable statutory requirements, Federal regulatory benchmarks, and widely recognized industry best practices for maritime cybersecurity.\n##### (b) Report\nThe Comptroller General shall submit the findings and recommendations from the review required under subsection (a) to\u2014\n**(1)**\nthe Committee on Commerce, Science, and Transportation, the Committee on Appropriations, and the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(2)**\nthe Committee on Transportation and Infrastructure, the Committee on Appropriations, and the Committee on Homeland Security of the House of Representatives.\n#### 4. Definitions\nIn this Act:\n**(1) Marine transportation system**\nThe term marine transportation system means navigable waterways, ports, terminals, intermodal connections, vessels, and related infrastructure that facilitate the movement of goods and people by water.\n**(2) Sector Risk Management Agency; SRMA**\nThe term Sector Risk Management Agency or SRMA has the meaning given the term Sector Risk Management Agency in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).",
      "versionDate": "2026-02-20",
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
        "updateDate": "2026-03-09T14:26:11Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7625ih.xml"
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
      "title": "MTS CYBER Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MTS CYBER Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Marine Transportation System Cybersecurity Budget and Evaluation Report Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Comptroller General of the United States to conduct a review of the budget, resources, and capabilities of the Coast Guard as the co-Sector Risk Management Agency for the marine transportation system.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T09:18:27Z"
    }
  ]
}
```

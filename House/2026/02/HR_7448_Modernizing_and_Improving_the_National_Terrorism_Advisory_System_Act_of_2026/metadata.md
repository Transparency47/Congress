# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7448?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7448
- Title: Modernizing and Improving the National Terrorism Advisory System Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7448
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-16T08:07:00Z
- Update date including text: 2026-05-16T08:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-02-10 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.
- 2026-02-10 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Hearings Held
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-02-10 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.
- 2026-02-10 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7448",
    "number": "7448",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000621",
        "district": "9",
        "firstName": "Nellie",
        "fullName": "Rep. Pou, Nellie [D-NJ-9]",
        "lastName": "Pou",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Modernizing and Improving the National Terrorism Advisory System Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:00Z",
    "updateDateIncludingText": "2026-05-16T08:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
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
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": [
                {
                  "date": "2026-05-14T18:10:42Z",
                  "name": "Reported by"
                },
                {
                  "date": "2026-05-14T18:10:20Z",
                  "name": "Hearings By (subcommittee)"
                },
                {
                  "date": "2026-02-10T14:58:29Z",
                  "name": "Referred to"
                }
              ]
            },
            "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
            "systemCode": "hshm05"
          },
          {
            "activities": {
              "item": {
                "date": "2026-02-10T19:08:52Z",
                "name": "Referred to"
              }
            },
            "name": "Cybersecurity and Infrastructure Protection Subcommittee",
            "systemCode": "hshm08"
          },
          {
            "activities": {
              "item": {
                "date": "2026-02-10T19:08:52Z",
                "name": "Referred to"
              }
            },
            "name": "Transportation and Maritime Security Subcommittee",
            "systemCode": "hshm07"
          }
        ]
      },
      "systemCode": "hshm00",
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
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TN"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7448ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7448\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Ms. Pou (for herself, Mr. Van Epps , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo direct the Secretary of Homeland Security to develop a strategy to modernize the National Terrorism Advisory System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing and Improving the National Terrorism Advisory System Act of 2026 .\n#### 2. Strategy to modernize the National Terrorism Advisory System\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a strategy to modernize the National Terrorism Advisory System (NTAS) (in this section referred to as the strategy ).\n##### (b) Considerations\nThe strategy shall consider the following:\n**(1)**\nDesignating a specific office or official within the Department of Homeland Security to oversee the NTAS.\n**(2)**\nThe criteria, protocols, and standard operating procedures for the issuance and sunset of NTAS bulletins and alerts.\n**(3)**\nThe public accessibility and use of NTAS bulletins and alerts.\n**(4)**\nThe effectiveness of the current NTAS in communicating timely and detailed information to the public about potential terrorism threats.\n**(5)**\nThe impact of NTAS bulletins and alerts on the ability of Federal, State, local, Tribal, and territorial law enforcement and emergency responders to prepare for, prevent, respond to, and mitigate against terrorism threats.\n**(6)**\nMechanisms to ensure NTAS bulletins and alerts reach the greatest number of people possible.\n##### (c) Engagement\nIn developing the strategy, the Secretary shall engage with individuals, stakeholders, the private sector, and Federal, State, local, Tribal, and territorial law enforcement and emergency responders to receive feedback on options to modernize the NTAS, including feedback related to the considerations under subsection (b).\n##### (d) Comptroller General review\nNot later than two years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on the implementation of this section.",
      "versionDate": "2026-02-09",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-19T15:58:41Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7448ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modernizing and Improving the National Terrorism Advisory System Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T04:23:21Z"
    },
    {
      "title": "Modernizing and Improving the National Terrorism Advisory System Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Homeland Security to develop a strategy to modernize the National Terrorism Advisory System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T04:18:25Z"
    }
  ]
}
```

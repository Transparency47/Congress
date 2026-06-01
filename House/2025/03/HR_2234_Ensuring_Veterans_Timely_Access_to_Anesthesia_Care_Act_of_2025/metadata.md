# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2234
- Title: Ensuring Veterans Timely Access to Anesthesia Care Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2234
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-05-15T08:07:42Z
- Update date including text: 2026-05-15T08:07:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Health.
- 2025-06-11 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Health.
- 2025-06-11 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2234",
    "number": "2234",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Ensuring Veterans Timely Access to Anesthesia Care Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:42Z",
    "updateDateIncludingText": "2026-05-15T08:07:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-04",
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
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": [
                {
                  "date": "2025-06-11T15:28:42Z",
                  "name": "Hearings By (subcommittee)"
                },
                {
                  "date": "2025-06-11T15:28:13Z",
                  "name": "Referred to"
                }
              ]
            },
            "name": "Economic Opportunity Subcommittee",
            "systemCode": "hsvr10"
          },
          {
            "activities": {
              "item": {
                "date": "2025-04-04T18:08:58Z",
                "name": "Referred to"
              }
            },
            "name": "Health Subcommittee",
            "systemCode": "hsvr03"
          }
        ]
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "VA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NE"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "IL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "MI"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-07",
      "state": "IN"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "OR"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "GA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "WI"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MS"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "OH"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "PA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "VT"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2234ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2234\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Ms. Underwood (for herself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to update certain standards regarding anesthesia and pain management services in the Veterans Health Administration.\n#### 1. Short title\nThis Act may be cited as the Ensuring Veterans Timely Access to Anesthesia Care Act of 2025 .\n#### 2. Alignment of standards regarding certified registered nurse anesthetists in the Veterans Health Administration with standards of the Defense Health Agency\nThe Secretary of Veterans Affairs shall update VHA Directive 1123 titled National Anesthesia Program, Department of Veterans Affairs Certified Registered Nurse Anesthetists Practice Guidelines (or any successor directive) to recognize, in the Veterans Health Administration, certified registered nurses anesthetists as licensed independent practitioners in a manner consistent with the practice standards described by section 3(f)(2) of Enclosure of Defense Health Agency Administrative Instruction 6025.07, dated November 8, 2023, as amended.\n#### 3. Requirements of anesthesia providers in the Veterans Health Administration\n##### (a) Certification\nThe Secretary of Veterans Affairs shall require an anesthesia professional employed by the Secretary as\u2014\n**(1)**\na physician anesthesiologist to be certified by the American Board of Anesthesiology or a similar body determined by the Secretary; and\n**(2)**\na certified registered nurse anesthetist to be certified by the Council on Certification of Nurse Anesthetists or the Council on Recertification of Nurse Anesthetists or a similar body determined by the Secretary.\n##### (b) Direct care\nThe Secretary shall require an anesthesia professional described in subsection (a) to have completed at least 25 hours of direct patient anesthesia care (not including supervision of other anesthesia professionals).\n##### (c) Enforcement\nThe Secretary shall suspend from employment in the Department of Veterans Affairs an anesthesia professional described in subsection (a) who has not complied with the requirements of this section.\n#### 4. GAO report on anesthesia delivery in the Veterans Health Administration\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Comptroller General of the United States shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that contains the following, and which shall be made publicly available:\n**(1)**\nData regarding outcomes regarding the following anesthesia models used in the Veterans Health Administration:\n**(A)**\nDelivery by an anesthesiologist.\n**(B)**\nDelivery by a certified registered nurse anesthetist under the supervision of a physician.\n**(C)**\nDelivery by a certified registered nurse anesthetist without supervision.\n**(2)**\nA comparison of the cost effectiveness of the models described in paragraph (1), including\u2014\n**(A)**\nthe estimated cost to medical facilities of the Department of Veterans Affairs and taxpayers for each such model; and\n**(B)**\na breakdown of costs and savings to taxpayers and to veterans\u2019 households associated with each such model.",
      "versionDate": "2025-03-18",
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
            "name": "Congressional oversight",
            "updateDate": "2025-06-27T16:06:16Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-06-27T16:06:02Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-06-27T16:05:57Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-06-27T16:06:08Z"
          },
          {
            "name": "Surgery and anesthesia",
            "updateDate": "2025-06-27T16:05:50Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-27T16:05:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T13:53:47Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2234ih.xml"
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
      "title": "Ensuring Veterans Timely Access to Anesthesia Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T12:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Veterans Timely Access to Anesthesia Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T12:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to update certain standards regarding anesthesia and pain management services in the Veterans Health Administration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T12:03:24Z"
    }
  ]
}
```

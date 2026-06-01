# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1793?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1793
- Title: Veterans Readiness and Employment Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1793
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-02-04T04:11:39Z
- Update date including text: 2026-02-04T04:11:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1793",
    "number": "1793",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Veterans Readiness and Employment Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T04:11:39Z",
    "updateDateIncludingText": "2026-02-04T04:11:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
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
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:02:50Z",
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
                "date": "2025-04-09T21:02:26Z",
                "name": "Reported by"
              },
              {
                "date": "2025-04-09T20:54:32Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-10T19:16:32Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-10T19:16:26Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NC"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MO"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "VA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "AR"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "IL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "MI"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "IN"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "OH"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MS"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MP"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "KY"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "DE"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "OR"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NV"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "VA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "KS"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1793ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1793\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Hamadeh of Arizona (for himself, Mr. Murphy , Mr. Jackson of Illinois , Mr. Ciscomani , Mr. Johnson of Georgia , Mr. Graves , Mr. Wittman , and Mr. Haridopolos ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for outreach requirements for Department of Veterans Affairs training and rehabilitation programs for veterans with service-connected disabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Readiness and Employment Transparency Act of 2025 .\n#### 2. Outreach requirements for Department of Veterans Affairs training and rehabilitation programs for veterans with service-connected disabilities\n##### (a) VRE contact information\nSection 3104 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(f) The Secretary shall establish a dedicated telephone number within the Education Call Center of the Department for calls about services provided under this chapter. Each regional office of the Department shall include, on the website of the regional office, a name, telephone number, and email address, through which veterans may receive information about services provided under this chapter. .\n##### (b) Outreach requirement\n**(1) In general**\nChapter 31 of title 38, United States Code, is amended by adding at the end the following new section:\n3123. Outreach requirements (a) Question and answer sessions The Secretary shall require each employee of the Department whose responsibilities include providing counseling and services under this chapter to attend a monthly question and answer session with appropriate school certifying officials. (b) Informational briefings (1) The Secretary shall require each veteran readiness and employment counselor to provide for veterans at each educational institution located in the geographic area served by the Regional Office where the counselor is employed an in-person briefing about services provided under this chapter. (2) The Secretary may provide a briefing required under paragraph (1) virtually in the case of an educational institution located more than 150 miles away from the headquarters of the Regional Office. (c) Annual report Not later than one year after the date of the enactment of this section, and annually thereafter, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the extension of periods of vocational rehabilitation programs under section 3105(c) of this title. Such report shall include, for the year covered by the report\u2014 (1) the number of veterans who requested such an extension; (2) the number of such requests that were approved; and (3) the number of such requests that were rejected. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by adding at the end the following new item:\n3123. Outreach requirements. .\n##### (c) Extension of entitlements\nSection 3105(c) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively;\n**(2)**\nby inserting (1) before The Secretary ; and\n**(3)**\nby adding at the end the following new paragraph:\n(2) If a veteran applies for an extension under paragraph (1), the Secretary shall approve or reject the extension by not later than 30 days after the date on which the veteran submits a request for the extension. .",
      "versionDate": "2025-03-03",
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
            "updateDate": "2025-04-01T15:27:58Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-04-01T15:27:52Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-04-01T15:27:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-26T15:09:22Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1793ih.xml"
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
      "title": "Veterans Readiness and Employment Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Readiness and Employment Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for outreach requirements for Department of Veterans Affairs training and rehabilitation programs for veterans with service-connected disabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:23Z"
    }
  ]
}
```

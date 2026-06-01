# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2605
- Title: SAVES Act
- Congress: 119
- Bill type: HR
- Bill number: 2605
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2026-03-10T17:06:22Z
- Update date including text: 2026-03-10T17:06:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-11 - Committee: Referred to the Subcommittee on Health.
- 2025-06-12 - Committee: Subcommittee Hearings Held
- 2025-07-03 - Committee: Subcommittee on Health Discharged
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- 2025-09-26 - Calendars: Placed on the Union Calendar, Calendar No. 264.
- 2025-09-26 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-310.
- 2025-09-26 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-310.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-11 - Committee: Referred to the Subcommittee on Health.
- 2025-06-12 - Committee: Subcommittee Hearings Held
- 2025-07-03 - Committee: Subcommittee on Health Discharged
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- 2025-09-26 - Calendars: Placed on the Union Calendar, Calendar No. 264.
- 2025-09-26 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-310.
- 2025-09-26 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-310.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2605",
    "number": "2605",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SAVES Act",
    "type": "HR",
    "updateDate": "2026-03-10T17:06:22Z",
    "updateDateIncludingText": "2026-03-10T17:06:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-09-26",
      "calendarNumber": {
        "calendar": "U00264"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 264.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-09-26",
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
      "text": "Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-310.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-310.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Health Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-04-11",
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
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
        "item": [
          {
            "date": "2025-09-26T14:32:00Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-23T16:34:24Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-03T17:23:06Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-04-02T22:00:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-12T16:39:54Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-04-11T16:39:39Z",
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
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "KY"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AZ"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "DC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "WI"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NC"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "TX"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CO"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AS"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "FL"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "VA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "SC"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "IA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "TN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MN"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "TX"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MP"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "VA"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MI"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "OH"
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "MN"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "IN"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "OH"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "MN"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NH"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "KS"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WI"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NV"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "WA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "AZ"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "FL"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "WA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "IL"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "PA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "OK"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MO"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "AL"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MS"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "AR"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "TX"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "MT"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "MS"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "GA"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2605ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2605\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Luttrell (for himself, Mr. McGarvey , Mr. Ciscomani , Mr. Buchanan , Ms. Norton , Mr. Van Orden , Mr. Murphy , Mr. Davis of North Carolina , Ms. Tenney , Mr. Hunt , Mr. Valadao , Mr. Crow , Mrs. Radewagen , Mr. Rutherford , Mrs. Kiggans of Virginia , Mr. Deluzio , Ms. Mace , Mrs. Miller-Meeks , Mr. Cohen , Mr. Lawler , Mr. Rulli , Mr. Stauber , Mr. Goldman of Texas , Mr. Pfluger , Ms. King-Hinds , and Mr. LaLota ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to award grants to nonprofit organizations to assist such organizations in carrying out programs to provide service dogs to eligible veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Service Dogs Assisting Veterans Act or the SAVES Act .\n#### 2. Department of Veterans Affairs pilot program to award grants for the provision of service dogs to veterans\n##### (a) In general\n**(1) Pilot program required**\nNot later than 24 months after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish a pilot program under which the Secretary shall award grants, on a competitive basis, to nonprofit entities to provide service dogs to eligible veterans.\n**(2) Duration**\nThe Secretary shall carry out the pilot program during the five-year period beginning on the date on which the first grant is awarded under this section.\n##### (b) Applications\n**(1) In general**\nTo be eligible to receive a grant under this section, a nonprofit entity shall submit an application to the Secretary at such time, in such manner, and containing such commitments and information as the Secretary may require.\n**(2) Elements**\nAn application submitted under paragraph (1) shall include the following:\n**(A)**\nA proposal for the provision of service dogs to eligible veterans, including how the nonprofit entity will communicate with the Secretary to ensure an increasing number of service dogs are provided to veterans.\n**(B)**\nA description of the following:\n**(i)**\nThe training that will be provided by the nonprofit entity to eligible veterans.\n**(ii)**\nThe training of dogs that will serve as service dogs.\n**(iii)**\nAny additional support or services the nonprofit entity will provide for such dogs and eligible veterans.\n**(iv)**\nThe plan for publicizing the availability of such dogs through a marketing campaign that targets eligible veterans.\n**(v)**\nThe commitment of the nonprofit entity to have humane standards for animals.\n**(C)**\nDocumentation that demonstrates that the nonprofit entity has experience in training dogs as service animals.\n##### (c) Award of grants\n**(1) In general**\nThe Secretary shall award a grant to each nonprofit entity for which the Secretary has approved an application submitted under subsection (b)(1).\n**(2) Agreement required**\nBefore the provision of any grant amounts to a nonprofit entity selected to receive a grant under this section, the Secretary shall enter into an agreement, containing such terms, conditions, and limitations as the Secretary determines appropriate, with such entity.\n**(3) Maximum grant amount**\nA grant under this section may not exceed $2,000,000.\n**(4) Payments**\nThe Secretary shall establish intervals of payment for the administration of each grant awarded under this section.\n##### (d) Use of funds\n**(1) In general**\nA recipient of a grant under this section shall use the grant amounts to plan, develop, implement, or manage (or any combination thereof) one or more programs that provide service dogs to eligible veterans.\n**(2) Administrative expenses**\nThe Secretary may establish a maximum amount for each grant awarded under this section that may be used by the recipient of the grant to cover administrative expenses.\n**(3) Other conditions and limitations**\nThe Secretary may establish other conditions or limitations on the use of grant amounts under this section.\n##### (e) Requirements for grant recipients\n**(1) Notifications and information**\nA recipient of a grant under this section shall\u2014\n**(A)**\nnotify each veteran who receives a service dog through such grant that the service dog is being paid for, in whole or in part, by the Department of Veterans Affairs; and\n**(B)**\ninform each such veteran of the benefits and services available from the Secretary for the veteran and the service dog.\n**(2) Prohibition on certain fees**\nA recipient of a grant under this section may not charge a fee to a veteran receiving a service dog through such grant.\n##### (f) Veterinary insurance\n**(1) In general**\nThe Secretary shall provide to each veteran who receives a service dog through a grant under this section a commercially available veterinary insurance policy for the service dog.\n**(2) Continuation**\nIf the Secretary provides a veterinary insurance policy to a veteran under paragraph (1), the Secretary shall continue to provide the policy to the veteran without regard to the continuation or termination of the pilot program.\n##### (g) Training and technical assistance\nThe Secretary may provide training and technical assistance to recipients of grants under this section.\n##### (h) Oversight and monitoring\n**(1) In general**\nThe Secretary\u2014\n**(A)**\nshall establish such oversight and monitoring requirements as the Secretary determines appropriate to ensure that grant amounts awarded under this section are used appropriately; and\n**(B)**\nmay take such actions as the Secretary determines necessary to address any issues identified through the enforcement of such requirements.\n**(2) Reports and answers**\nThe Secretary may require each recipient of a grant under this section to provide, in such form as may be prescribed by the Secretary, such reports or answers in writing to specific questions, surveys, or questionnaires as the Secretary determines necessary to carry out the pilot program.\n##### (i) Definitions\nIn this section:\n**(1)**\nThe term eligible veteran means a veteran who has a covered condition=.\n**(2)**\nThe term covered condition means any of the following:\n**(A)**\nBlindness or visual impairment.\n**(B)**\nLoss of use of a limb, paralysis, or other significant mobility issue, including mental health mobility.\n**(C)**\nLoss of hearing.\n**(D)**\nPost-traumatic stress disorder.\n**(E)**\nTraumatic brain injury.\n**(F)**\nAny other disability, condition, or diagnosis for which the Secretary determines, based on medical judgment, that it is optimal for the veteran to manage the disability, condition, or diagnosis, and live independently through the assistance of a service dog.\n**(3)**\nThe term service animal has the meaning given such term in section 36.104 of title 28, Code of Federal Regulations (or successor regulation).\n**(4)**\nThe term service dog means any dog that is individually trained to do work or perform tasks that are\u2014\n**(A)**\nfor the benefit of a veteran with a covered condition; and\n**(B)**\ndirectly related to the covered condition of the veteran.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of the five consecutive fiscal years following the fiscal year in which the pilot program is established under subsection (a).",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2605rh.xml",
      "text": "IB\nUnion Calendar No. 264\n119th CONGRESS\n1st Session\nH. R. 2605\n[Report No. 119\u2013310]\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Luttrell (for himself, Mr. McGarvey , Mr. Ciscomani , Mr. Buchanan , Ms. Norton , Mr. Van Orden , Mr. Murphy , Mr. Davis of North Carolina , Ms. Tenney , Mr. Hunt , Mr. Valadao , Mr. Crow , Mrs. Radewagen , Mr. Rutherford , Mrs. Kiggans of Virginia , Mr. Deluzio , Ms. Mace , Mrs. Miller-Meeks , Mr. Cohen , Mr. Lawler , Mr. Rulli , Mr. Stauber , Mr. Goldman of Texas , Mr. Pfluger , Ms. King-Hinds , and Mr. LaLota ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nSeptember 26, 2025 Additional sponsors: Mr. Vindman , Mr. Barrett , Mr. Conaway , Ms. Malliotakis , Mr. Miller of Ohio , Ms. Bynum , Mr. Finstad , Mr. Yakym , Mrs. Sykes , Ms. Morrison , Ms. Goodlander , Mr. Schmidt , Mr. Casten , Mr. Kennedy of New York , Mr. Wied , Mr. Smith of Washington , Ms. Lee of Nevada , Mr. Mannion , Mr. Neguse , Ms. DelBene , Mr. Crane , Mr. Haridopolos , Mr. Larsen of Washington , Ms. Budzinski , Mr. Thompson of California , Mr. Gray , Mr. Reschenthaler , Ms. Salazar , Mr. Crenshaw , Mrs. Bice , Mr. Bell , Ms. Escobar , Mr. McGuire , Mr. Moran , Mr. Weber of Texas , Mr. Cuellar , Mr. Tony Gonzales of Texas , Mr. Strong , Mr. Kelly of Mississippi , Mr. Gooden , Mr. Womack , Mr. Nehls , Mr. Zinke , Mr. McCaul , Mr. Ezell , Mr. Babin , Mr. Ellzey , Mr. Collins , Mr. Williams of Texas , Mr. Fallon , and Mr. Nunn of Iowa\nSeptember 26, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on April 2, 2025\nA BILL\nTo require the Secretary of Veterans Affairs to award grants to nonprofit organizations to assist such organizations in carrying out programs to provide service dogs to eligible veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Service Dogs Assisting Veterans Act or the SAVES Act .\n#### 2. Department of Veterans Affairs pilot program to award grants for the provision of service dogs to veterans\n##### (a) In general\nNot later than 24 months after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish a pilot program under which the Secretary shall award grants, on a competitive basis, to nonprofit entities to provide service dogs to eligible veterans.\n##### (b) Applications\n**(1) In general**\nTo be eligible to receive a grant under this section, a nonprofit entity shall submit an application to the Secretary at such time, in such manner, and containing such commitments and information as the Secretary may require.\n**(2) Elements**\nAn application submitted under paragraph (1) shall include the following:\n**(A)**\nA proposal for the provision of service dogs to eligible veterans, including how the nonprofit entity will communicate with the Secretary to ensure that the use of the grant funds results in an increased number of eligible veterans who are provided with service dogs.\n**(B)**\nA description of the following services or commitments to be provided by the nonprofit entity:\n**(i)**\nThe training that will be provided to eligible veterans who receive service dogs under the pilot program.\n**(ii)**\nThe training of dogs that will serve as service dogs provided to eligible veterans under the program.\n**(iii)**\nAny support or services other than training under clauses (i) and (ii) that will be provided for such dogs and eligible veterans.\n**(iv)**\nThe plan for publicizing the availability of such service dogs through a marketing campaign that targets eligible veterans.\n**(v)**\nThe commitment to humane treatment standards for service dogs.\n**(C)**\nDocumentation that demonstrates that the nonprofit entity has experience in training dogs as service dogs.\n**(D)**\nThe demonstrated experience of the nonprofit entity in training service dogs in compliance with the requirements of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n##### (c) Agreement required\nIf the Secretary approves an application submitted by a nonprofit entity under subsection (b)(1), the Secretary shall require the entity, as a condition of the receipt of a grant under the pilot program to enter into an agreement under which the entity agrees to\u2014\n**(1)**\nnotify each veteran who receives a service dog provided using grant funds that the service dog is being paid for, in whole or in part, by the Department of Veterans Affairs;\n**(2)**\ninform each such veteran of the benefits and services available from the Secretary for the veteran and the service dog;\n**(3)**\nnot charge a fee to a veteran receiving a service dog provided using grant funds; and\n**(4)**\nadhere to such other terms, conditions, and limitations as the Secretary determines appropriate.\n##### (d) Amount of grants\nThe Secretary shall make a grant in an amount that does not exceed $2,000,000 to each entity that enters into an agreement with the Secretary under subsection (c). The Secretary shall establish intervals of payment for the administration of each such grant.\n##### (e) Use of funds\n**(1) In general**\nA recipient of a grant under this section shall use the grant to plan, develop, implement, and manage one or more programs that provide service dogs to eligible veterans.\n**(2) Limitations**\nThe Secretary may establish\u2014\n**(A)**\na maximum amount that can be used by a grant recipient to cover administrative expenses for each grant awarded under this section; and\n**(B)**\nother conditions or limitations on the use of grant amounts under this section.\n##### (f) Veterinary insurance\n**(1) In general**\nExcept as provided in paragraph (3), the Secretary may provide to each veteran who receives a service dog through a grant under this section a commercially available veterinary insurance policy for the service dog.\n**(2) Continuation**\nIf the Secretary provides a veterinary insurance policy to a veteran under paragraph (1), the Secretary shall continue to provide the policy to the veteran without regard to the continuation or termination of the pilot program, except as provided in paragraph (3).\n**(3) Discontinuation**\nThe Secretary shall discontinue the provision of a veterinary insurance policy under paragraph (1) if the Secretary determines doing so would be in the best interest of the veteran, the service dog, or the Federal Government.\n##### (g) Training and technical assistance\nThe Secretary may provide training and technical assistance related to grant application and administration to applicants for and recipients of grants under this section.\n##### (h) Oversight and monitoring\n**(1) In general**\nThe Secretary\u2014\n**(A)**\nshall establish such oversight and monitoring requirements as the Secretary determines appropriate to ensure that grant amounts awarded under this section are used appropriately; and\n**(B)**\nmay take such actions as the Secretary determines necessary to address any issues identified through the enforcement of such requirements.\n**(2) Reports and answers**\nThe Secretary may require each recipient of a grant under this section to provide, in such form as may be prescribed by the Secretary, such reports or answers in writing to specific questions, surveys, or questionnaires as the Secretary determines necessary to carry out the pilot program.\n##### (i) Definitions\nIn this section:\n**(1)**\nThe term eligible veteran means a veteran who\u2014\n**(A)**\nis enrolled in the system of annual patient enrollment of the Department of Veterans Affairs established and operated under section 1705(a) of title 38, United States Code, or is otherwise entitled to receive such care and services under subsection (c)(2) of such section;\n**(B)**\nhas been prescribed a service dog by the Secretary; and\n**(C)**\nhas one or more covered conditions.\n**(2)**\nThe term covered condition means any of the following disabilities, conditions, or diagnoses for which the Secretary determines, based upon medical judgment, that it is optimal for the veteran to manage the disability, condition, or diagnosis and live independently through the assistance of a trained service dog:\n**(A)**\nBlindness or visual impairment.\n**(B)**\nLoss of use of a limb, paralysis, or other significant mobility issue, including mental health mobility.\n**(C)**\nLoss of hearing.\n**(D)**\nPost-traumatic stress disorder.\n**(E)**\nTraumatic brain injury.\n**(F)**\nAny other disability, condition, or diagnosis for which the Secretary determines, based on medical judgment, that it is optimal for the veteran to manage the disability, condition, or diagnosis, and live independently through the assistance of a service dog.\n**(3)**\nThe term service dog means a dog that is individually trained to do work or perform tasks for the benefit of an individual with a disability, including a physical, sensory, psychiatric, intellectual, or other mental disability.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2027 through 2031.\n##### (k) Termination\nThe authority to carry out a pilot program under this section shall terminate on September 30, 2031.\n#### 3. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking November 30, 2031 and inserting February 28, 2033 .",
      "versionDate": "2025-09-26",
      "versionType": "Reported in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-24",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 342."
      },
      "number": "1441",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "House",
            "type": "Related bill"
          },
          {
            "identifiedBy": "CRS",
            "type": "Related bill"
          }
        ]
      },
      "title": "SAVES Act of 2025",
      "type": "S"
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
            "name": "Disability assistance",
            "updateDate": "2025-06-23T20:08:50Z"
          },
          {
            "name": "Service animals",
            "updateDate": "2025-06-23T20:08:50Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-06-23T20:08:50Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-23T20:08:50Z"
          },
          {
            "name": "Veterinary medicine and animal diseases",
            "updateDate": "2025-06-23T20:08:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T14:07:15Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2605ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2605rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "SAVES Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-27T03:23:13Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Service Dogs Assisting Veterans Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-27T03:23:13Z"
    },
    {
      "title": "SAVES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAVES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Service Dogs Assisting Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to award grants to nonprofit organizations to assist such organizations in carrying out programs to provide service dogs to eligible veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T11:18:23Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5362?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5362
- Title: To name the Department of Veterans Affairs multispecialty clinic in Marietta, Georgia, as the "Colonel Michael H. Boyce Department of Veterans Affairs Multispecialty Clinic".
- Congress: 119
- Bill type: HR
- Bill number: 5362
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2025-10-04T08:05:31Z
- Update date including text: 2025-10-04T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-09-25 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-09-15: Introduced in House

## Actions

- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-09-25 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5362",
    "number": "5362",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "To name the Department of Veterans Affairs multispecialty clinic in Marietta, Georgia, as the \"Colonel Michael H. Boyce Department of Veterans Affairs Multispecialty Clinic\".",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:31Z",
    "updateDateIncludingText": "2025-10-04T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-25",
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
      "actionDate": "2025-09-15",
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
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-25T17:10:58Z",
              "name": "Referred to"
            }
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5362ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5362\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Mr. Loudermilk (for himself, Mr. McCormick , Mr. Johnson of Georgia , Mr. Carter of Georgia , Mrs. McBath , Mr. David Scott of Georgia , Mr. Austin Scott of Georgia , Mr. Allen , Mr. Jack , Mr. Clyde , Mr. Collins , Ms. Williams of Georgia , Ms. Greene of Georgia , and Mr. Bishop ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo name the Department of Veterans Affairs multispecialty clinic in Marietta, Georgia, as the Colonel Michael H. Boyce Department of Veterans Affairs Multispecialty Clinic .\n#### 1. Findings\nCongress finds the following:\n**(1)**\nColonel Mike Boyce was born on September 1, 1949, in Brawley, California.\n**(2)**\nMike Boyce graduated from the University of Notre Dame in 1971, and was commissioned as a 2d Lieutenant in the United States Marine Corps in 1971.\n**(3)**\nAfter completing Marine Corps Basic School and the U.S. Army Field Artillery School in 1972, Mike Boyce was assigned to the 1st Marine Division at Camp Pendleton, California.\n**(4)**\nThroughout his service, Colonel Mike Boyce was also assigned to the 2nd Marine Aircraft Wing at Marine Corps Air Station New River, the 1st Marine Air Wing in Okinawa, the 4th Marine Air Wing at Naval Air Station Andrews, Korea, and the 1st Marine Expeditionary Brigade in Kaneohe Bay, Hawaii.\n**(5)**\nAfter completing attach\u00e9 training, Mike Boyce was assigned to Ankara, Turkey, in support of Operations Desert Shield, Desert Storm, and Provide Comfort. He was later assigned to Marine Air Group-16 for deployment to Somalia for Operation Restore Hope.\n**(6)**\nBefore his retirement in 2001, Colonel Mike Boyce served as Head Programmer for OPNAV N88, the Deputy Commander of Marine Corps Base Hawaii, Head of Operational Plans at MARFORPAC, and served in Bahrain and Oman in support of Operations Desert Thunder and Desert Fox.\n**(7)**\nAfter his service, Colonel Mike Boyce moved to Marietta, Georgia, and was active in his community. Colonel Mike Boyce served multiple charities including Habitat for Humanity, MUST Ministries, and the United Service Organizations.\n**(8)**\nA dedicated member of his church, Colonel Mike Boyce served in the men\u2019s ministry, youth programs, led Bible studies, and helped create the veterans\u2019 ministry.\n**(9)**\nColonel Mike Boyce was an active member of American Legion Post 29, the Marine Corps League, Veterans of Foreign Wars, Disabled American Veterans, and the Military Officers Association of America.\n**(10)**\nColonel Mike Boyce served as the chairman of the Cobb County Board of Commissioners from 2016 until 2020. During that time, he led the effort to make Veterans Day a paid holiday for county employees and was instrumental in establishing the first Veterans Service Office in Cobb County. He also led the effort to have the first Department of Veterans Affairs clinic established in Cobb County so veterans would have an easier experience seeking medical care.\n**(11)**\nColonel Mike Boyce died on January 25, 2022, in South Bend, Indiana, and is survived by his wife, Judy Moon Boyce, and his children Alison Boyce Cotsonika, Kevin Reid Boyce, and Sean Michael Boyce.\n#### 2. Name of Department of Veterans Affairs multispecialty clinic, Marietta, Georgia\nThe Department of Veterans Affairs multispecialty clinic located at 1263 Cobb Parkway NW, Marietta, Georgia, shall after the date of the enactment of this Act be known and designated as the Colonel Michael H. Boyce Department of Veterans Affairs Multispecialty Clinic or the Colonel Michael H. Boyce VA Clinic . Any reference to such multispecialty clinic in any law, regulation, map, document, paper, or other record of the United States shall be considered to be a reference to the Colonel Michael H. Boyce VA Multispecialty Clinic.",
      "versionDate": "2025-09-15",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-24T15:19:28Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5362ih.xml"
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
      "title": "To name the Department of Veterans Affairs multispecialty clinic in Marietta, Georgia, as the \"Colonel Michael H. Boyce Department of Veterans Affairs Multispecialty Clinic\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:20Z"
    },
    {
      "title": "To name the Department of Veterans Affairs multispecialty clinic in Marietta, Georgia, as the \"Colonel Michael H. Boyce Department of Veterans Affairs Multispecialty Clinic\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T08:06:14Z"
    }
  ]
}
```

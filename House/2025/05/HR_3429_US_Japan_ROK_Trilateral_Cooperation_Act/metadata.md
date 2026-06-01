# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3429?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3429
- Title: US-Japan-ROK Trilateral Cooperation Act
- Congress: 119
- Bill type: HR
- Bill number: 3429
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-12-02T09:05:39Z
- Update date including text: 2025-12-02T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 47 - 3.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 47 - 3.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3429",
    "number": "3429",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001287",
        "district": "6",
        "firstName": "Ami",
        "fullName": "Rep. Bera, Ami [D-CA-6]",
        "lastName": "Bera",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "US-Japan-ROK Trilateral Cooperation Act",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:39Z",
    "updateDateIncludingText": "2025-12-02T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 47 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
            "date": "2025-07-22T15:34:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-15T14:02:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "SC"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NE"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "HI"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "MP"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "GU"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "VA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "WA"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "AS"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "DE"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "IL"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3429ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3429\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Bera (for himself, Mr. Wilson of South Carolina , Mr. Connolly , Mr. Kelly of Pennsylvania , Mr. Castro of Texas , and Mr. Smith of Nebraska ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo establish an inter-parliamentary dialogue to facilitate closer cooperation between the United States, Japan, and the Republic of Korea on shared interests and values.\n#### 1. Short title\nThis Act may be cited as the US-Japan-ROK Trilateral Cooperation Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States should continue to strengthen trilateral cooperation between the United States, Japan, and the Republic of Korea (in this Act referred to as the ROK ) to enhance and implement a shared vision to meet regional challenges and to promote a free, open, inclusive, resilient, and healthy Indo-Pacific region;\n**(2)**\nthe historic Camp David summit on August 18, 2023, marked a new era of trilateral partnership between the United States, Japan, and the ROK, reaffirming their commitment to align collective efforts for regional security and prosperity;\n**(3)**\nthe Spirit of Camp David, as outlined in the joint statement, should guide future trilateral cooperation, emphasizing shared values, strategic alignment, and commitment to regional peace and stability;\n**(4)**\nthe United States, Japan, and the ROK should enhance Trilateral Maritime Security Cooperation to promote stability and freedom of navigation in the Indo-Pacific region;\n**(5)**\nthe United States, Japan, and the ROK should collaborate on countering foreign information manipulation and interference to protect democratic institutions and promote accurate information sharing;\n**(6)**\nPresident Biden\u2019s decision to elevate the US-Japan-ROK trilateral partnership to the leaders level was critical to bolstering cooperation, and all three countries should work to ensure that the Trilateral Leaders\u2019 Summit continues to take place regularly;\n**(7)**\nthe ambitious framework for ongoing cooperation laid out by the three leaders at the historic Camp David summit on August 18, 2023, should continue and be strengthened; and\n**(8)**\nthe formation of a regular US-Japan-ROK Inter-Parliamentary Dialogue will\u2014\n**(A)**\nsustain and deepen engagement between senior officials of the three countries on a full spectrum of issues; and\n**(B)**\nbe modeled on the successful and long-standing bilateral inter-parliamentary groups between the United States and other allied nations.\n#### 3. Establishment of US-Japan-ROK Inter-Parliamentary Dialogue\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in consultation with Congress, shall seek to enter into negotiations with the Governments of Japan and the ROK with the goal of reaching a written agreement to establish a US-Japan-ROK Inter-Parliamentary Dialogue to facilitate closer cooperation on shared interests and values.\n##### (b) United States Group\n**(1) In general**\nAt such time as the governments of the United States, Japan, and ROK enter into a written agreement described in subsection (a) to establish a US-Japan-ROK Inter-Parliamentary Dialogue, there shall be established a United States Group, which shall represent the United States at the US-Japan-ROK Inter-Parliamentary Dialogue.\n**(2) Membership**\n**(A) In general**\nThe United States Group shall be comprised of not more than 8 Members of Congress.\n**(B) Appointment**\nOf the Members of Congress appointed to the United States Group under subparagraph (A)\u2014\n**(i)**\ntwo shall be appointed by the Speaker of the House of Representatives, from among Members of the House, not fewer than one of whom shall be a member of the Committee on Foreign Affairs;\n**(ii)**\ntwo shall be appointed by the House Minority Leader, from among Members of the House, not fewer than one of whom shall be a member of the Committee on Foreign Affairs;\n**(iii)**\ntwo shall be appointed by the Senate Majority Leader, from among Members of the Senate, not fewer than one of whom shall be a member of the Committee on Foreign Relations; and\n**(iv)**\ntwo shall be appointed by the Senate Minority Leader, from among Members of the Senate, not fewer than one of whom shall be a member of the Committee on Foreign Relations.\n**(C) Term**\nAppointments to the United States Group shall be for the duration of two years.\n**(3) Meetings**\n**(A) In general**\nThe United States Group shall seek to meet not less frequently than annually with representatives and appropriate staff of the legislatures of Japan and the ROK, and representatives and appropriate staff of any other country invited by mutual agreement of the three countries.\n**(B) Limitation**\nA meeting described in subparagraph (A) may be held\u2014\n**(i)**\nin the United States;\n**(ii)**\nin another country during periods when Congress is not in session; or\n**(iii)**\nvirtually.\n**(4) Chairperson and Vice Chairperson**\n**(A) Rotation**\nThe positions of Chairperson and Vice Chairperson of the United States Group shall alternate between the House and Senate delegations every two years, coinciding with each new Congress.\n**(B) House delegation**\n**(i)**\nIn Congresses with an odd number, the Speaker of the House of Representatives shall designate the Chairperson of the United States Group from among members of the House delegation who are also members of the Committee on Foreign Affairs.\n**(ii)**\nIn Congresses with an even number, the Speaker of the House of Representatives shall designate the Vice Chairperson of the United States Group from among members of the House delegation who are also members of the Committee on Foreign Affairs.\n**(C) Senate delegation**\n**(i)**\nIn Congresses with an even number, the President Pro Tempore of the Senate shall designate the Chairperson of the United States Group from among members of the Senate delegation who are also members of the Committee on Foreign Relations.\n**(ii)**\nIn Congresses with an odd number, the President Pro Tempore of the Senate shall designate the Vice Chairperson of the United States Group from among members of the Senate delegation who are also members of the Committee on Foreign Relations.\n**(D) Term**\nThe Chairperson and Vice Chairperson shall serve for the duration one each Congress.\n**(5) Private sources**\nThe United States Group may accept gifts or donations of services or property, subject to the review and approval, as appropriate, of the Committee on Ethics of the House of Representatives and the Committee on Ethics of the Senate.\n**(6) Certification of expenditures**\nThe certificate of the chairperson of the delegation from the House of Representatives or the delegation of the Senate of the United States Group shall be final and conclusive upon the accounting officers in the auditing of the accounts of the United States Group.\n**(7) Annual report**\nThe United States Group shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report for each fiscal year for which an appropriation is made for the United States Group, which shall include its expenditures under such appropriation and a description thereof.",
      "versionDate": "2025-05-15",
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
            "name": "Advisory bodies",
            "updateDate": "2025-08-19T13:31:02Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-08-19T13:30:56Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-19T13:31:26Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-08-19T13:31:21Z"
          },
          {
            "name": "Japan",
            "updateDate": "2025-08-19T13:30:50Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-08-19T13:31:08Z"
          },
          {
            "name": "South Korea",
            "updateDate": "2025-08-19T13:30:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-20T13:55:41Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3429ih.xml"
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
      "title": "US-Japan-ROK Trilateral Cooperation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "US-Japan-ROK Trilateral Cooperation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish an inter-parliamentary dialogue to facilitate closer cooperation between the United States, Japan, and the Republic of Korea on shared interests and values.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:18Z"
    }
  ]
}
```

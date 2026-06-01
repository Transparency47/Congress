# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7661
- Title: Stop the Sexualization of Children Act
- Congress: 119
- Bill type: HR
- Bill number: 7661
- Origin chamber: House
- Introduced date: 2026-02-24
- Update date: 2026-04-28T08:06:11Z
- Update date including text: 2026-04-28T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 13.
- Latest action: 2026-02-24: Introduced in House

## Actions

- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 13.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7661",
    "number": "7661",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Stop the Sexualization of Children Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:11Z",
    "updateDateIncludingText": "2026-04-28T08:06:11Z"
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
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-24",
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
            "date": "2026-03-17T19:36:29Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-24T15:00:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "MT"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TN"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "WY"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "AL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "SC"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "LA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TN"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "UT"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
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
      "sponsorshipDate": "2026-03-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7661ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7661\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2026 Mrs. Miller of Illinois (for herself, Mr. Downing , Mr. Fine , Mr. Steube , Mr. Gosar , Mr. Ogles , Ms. Hageman , Mr. Stutzman , Mr. Moore of Alabama , Mrs. Biggs of South Carolina , Ms. Letlow , Ms. Tenney , Mr. Roy , Mr. Davidson , Mr. Weber of Texas , Mr. Rose , Mr. Owens , and Mr. Self ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to prohibit the use of funds provided under such Act to develop, implement, facilitate, host, or promote any program or activity for, or to provide or promote literature or other materials to, children under the age of 18 that includes sexually oriented material, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop the Sexualization of Children Act .\n#### 2. Prohibiting funding for sexually oriented material\nSection 8526 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7906 ) is amended\u2014\n**(1)**\nby striking No funds under this Act may be used\u2014 and inserting the following:\n(a) General prohibitions No funds under this Act may be used\u2014 ; and\n**(2)**\nby adding at the end the following:\n(b) Prohibiting funding for sexually oriented material (1) In general No funds under this Act may be used to develop, implement, facilitate, host, or promote any program or activity for, or to provide or promote literature or other materials to, children under the age of 18 that includes sexually oriented material, including any program, activity, literature, or material that exposes such children to nude adults, individuals who are stripping, or lewd or lascivious dancing. (2) Rule of construction Nothing in this subsection shall be construed to prohibit the use of funds under this Act for, or otherwise limit or interfere with, teaching\u2014 (A) standard science coursework, including biology, botany, zoology, microbiology, cytology, genetics, ecology, human health, or human anatomy and physiology; (B) the texts of major world religions; (C) classic works of literature; or (D) classic works of art. (3) Definitions In this subsection: (A) Classic works of art The term classic works of art means the works of art depicted, referenced, or otherwise represented in Smarthistory guide to AP Art History, volumes 1, 2, 3, 4, and 5 (2019\u20132020), published by Smarthistory. (B) Classic works of literature The term classic works of literature means the works of literature (including translations of such works)\u2014 (i) included in the Great Books of the Western World (second edition, 1990), published by Encyclopaedia Britannica; (ii) referenced in the article Classics Every Middle Schooler Should Read by Thomas Purifoy, Jr. and published by Compass Classroom (as such article appeared on the date of enactment of this subsection); and (iii) referenced in the article Classics Every High Schooler Should Read by Mary Pierson Purifoy and published by Compass Classroom (as such article appeared on the date of enactment of this subsection). (C) Sexually oriented material The term sexually oriented material means material that\u2014 (i) includes any depiction, description, or simulation of sexually explicit conduct (as defined in subparagraphs (A) and (B) of section 2256(2) of title 18, United States Code); or (ii) involves gender dysphoria or transgenderism. .",
      "versionDate": "2026-02-24",
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
            "name": "Education programs funding",
            "updateDate": "2026-04-02T18:46:00Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-04-02T18:45:51Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2026-04-02T18:46:05Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-04-02T18:45:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-03-02T18:05:06Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7661ih.xml"
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
      "title": "Stop the Sexualization of Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop the Sexualization of Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to prohibit the use of funds provided under such Act to develop, implement, facilitate, host, or promote any program or activity for, or to provide or promote literature or other materials to, children under the age of 18 that includes sexually oriented material, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T09:18:37Z"
    }
  ]
}
```

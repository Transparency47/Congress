# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6289
- Title: Promoting a Safe Internet for Minors Act
- Congress: 119
- Bill type: HR
- Bill number: 6289
- Origin chamber: House
- Introduced date: 2025-11-25
- Update date: 2026-05-14T08:08:35Z
- Update date including text: 2026-05-14T08:08:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-25: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-11-25: Introduced in House

## Actions

- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-25",
    "latestAction": {
      "actionDate": "2025-11-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6289",
    "number": "6289",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Promoting a Safe Internet for Minors Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:35Z",
    "updateDateIncludingText": "2026-05-14T08:08:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
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
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
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
      "actionDate": "2025-11-25",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-25",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-25",
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
          "date": "2025-11-25T16:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-11T21:29:29Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:29:16Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-25T21:29:05Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "FL"
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
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6289ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6289\nIN THE HOUSE OF REPRESENTATIVES\nNovember 25, 2025 Ms. Lee of Florida (for herself and Mr. Soto ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Children\u2019s Online Privacy Protection Act of 1998 to promote online safety for minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting a Safe Internet for Minors Act .\n#### 2. Online safety for minors\n##### (a) Amendment\nSubtitle A of the Protecting Children in the 21st Century Act ( 15 U.S.C. 6551 et seq. ) is amended by striking sections 211 through 214 and 216 and inserting the following:\n211. Public awareness and educational campaign Not later than 180 days after the date of the enactment of this section, the Commission, in partnership with the heads of other relevant agencies, State and local governments, nonprofit organizations, schools, industry, law enforcement, medical professionals, and other appropriate entities, shall carry out a program throughout the United States to promote the safe use of the internet by minors, that includes the following: (1) The identification, promotion, and encouragement of best practices for educators, online platforms, minors, and parents and guardians to protect minors online. (2) The establishment and implementation of an outreach and education campaign throughout the United States that promotes online safety for minors. (3) The facilitation of access to, and the exchange of, information regarding online safety for minors to promote up-to-date knowledge regarding harms and risks negatively impacting or benefits positively impacting minors online. (4) The facilitation of access to publicly accessible online safety education and public awareness efforts by other relevant agencies, State and local governments, nonprofit organizations, schools, industry, and other appropriate entities. 212. Annual report Not later than 1 year after the date of the enactment of this section, and annually thereafter for 10 years, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that describes the activities carried out under section 211. 213. Definitions In this subtitle: (1) Agency The term agency has the meaning given that term in section 551 of title 5, United States Code. (2) Commission The term Commission means the Federal Trade Commission. (3) Minor The term minor means an individual under the age of 17. (4) Nonprofit organization The term nonprofit organization means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code. (5) Online safety The term online safety includes issues regarding the use of the internet in a manner that promotes safe online activity for minors through the following: (A) Protecting minors from cybercrimes, access to narcotics, tobacco products, gambling, alcohol, and other adult content. (B) Preventing compulsive behavior online and other adverse impacts on the physical and mental health of minors. (C) Facilitating the effective use of safeguards, parental controls, and other tools to empower parents, guardians, and minors to protect minors online. (6) State The term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe. .\n##### (b) Technical and conforming amendments\nThe table of contents for subtitle A of the Protecting Children in the 21st Century Act ( 15 U.S.C. 6551 et seq. ) is amended\u2014\n**(1)**\nby striking the items related to sections 211 through 214 and 216; and\n**(2)**\ninserting before section 215 the following:\nSec. 211. Public awareness and educational campaign. Sec. 212. Annual report. Sec. 213. Definitions. .",
      "versionDate": "2025-11-25",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7757",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "KIDS Act",
      "type": "HR"
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
            "name": "Child safety and welfare",
            "updateDate": "2026-01-07T18:06:58Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-07T18:17:46Z"
          },
          {
            "name": "Educational guidance",
            "updateDate": "2026-01-07T18:15:21Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-07T18:10:15Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-01-07T18:15:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-09T22:20:52Z"
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
      "date": "2025-11-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6289ih.xml"
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
      "title": "Promoting a Safe Internet for Minors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-26T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting a Safe Internet for Minors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Children's Online Privacy Protection Act of 1998 to promote online safety for minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T09:18:22Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/134?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/134
- Title: Protecting our Communities from Sexual Predators Act
- Congress: 119
- Bill type: HR
- Bill number: 134
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-09-18T08:07:07Z
- Update date including text: 2025-09-18T08:07:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/134",
    "number": "134",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Protecting our Communities from Sexual Predators Act",
    "type": "HR",
    "updateDate": "2025-09-18T08:07:07Z",
    "updateDateIncludingText": "2025-09-18T08:07:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:25:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MN"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "AZ"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr134ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 134\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Buchanan (for himself, Mr. Issa , Mr. Stauber , Mr. McCaul , Mr. Bost , Mr. Weber of Texas , and Mr. Edwards ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to provide for the detention, inadmissibility, and removal of aliens who commit sexual assault.\n#### 1. Short title\nThis Act may be cited as the Protecting our Communities from Sexual Predators Act .\n#### 2. Detention of certain aliens who commit sexual assault\nSection 236(c)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c)(1) ) is amended\u2014\n**(1)**\nin subparagraph (C), by striking , or and inserting a comma;\n**(2)**\nin subparagraph (D), by adding or at the end; and\n**(3)**\nby inserting after subparagraph (D) the following:\n(E) (i) is inadmissible under section 212(a)(6)(A) or (C) or under section 212(a)(7); and (ii) is charged with, arrested for, convicted of, admits having committed, or admits committing acts which constitute the essential elements of, any offense involving sexual assault (as such term is defined in section 214(d)(3)(A)), .\n#### 3. Inadmissilibity and deportability related to sexual assault\n##### (a) Inadmissibility\nSection 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ) is amended by adding at the end the following:\n(J) Sexual assault Any alien who has been convicted of, who admits having committed, or who admits committing acts which constitute the essential elements of, any offense involving sexual assault (as such term is defined in section 214(d)(3)(A)), is inadmissible. .\n##### (b) Deportability\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Sexual assault Any alien who has been convicted of, who admits having committed, or who admits committing acts which constitute the essential elements of, any offense involving sexual assault (as such term is defined in section 214(d)(3)(A)), is deportable. .",
      "versionDate": "2025-01-03",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-09-17T20:59:26Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-09-17T21:06:51Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-09-17T20:59:36Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-09-17T20:36:42Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-09-17T20:36:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-01-31T14:16:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr134",
          "measure-number": "134",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr134v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting our Communities from Sexual Predators Act</strong></p><p>This bill requires the Department of Justice (DOJ) to detain certain non-U.S. nationals (<em>aliens</em> under federal law) who have been arrested for sexual assault. The bill also provides for the inadmissibility and deportability of certain individuals convicted of sexual assault.</p><p>Under this bill, the DOJ must detain an individual who (1) is unlawfully present in the United States, made certain misrepresentations, or did not possess the necessary documents when applying for admission; and (2) has been charged with, arrested for, convicted of, or admits to having committed acts which constitute the essential elements of, an offense involving sexual assault.</p><p>The bill also establishes under statute that a conviction for certain crimes related to sexual assault shall be grounds for (1) barring an individual from entering the United States, and (2) deportability. (Under current law, convictions for certain crimes, including crimes involving moral turpitude, are grounds for inadmissibility and deportability.)\u00a0</p>"
        },
        "title": "Protecting our Communities from Sexual Predators Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr134.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting our Communities from Sexual Predators Act</strong></p><p>This bill requires the Department of Justice (DOJ) to detain certain non-U.S. nationals (<em>aliens</em> under federal law) who have been arrested for sexual assault. The bill also provides for the inadmissibility and deportability of certain individuals convicted of sexual assault.</p><p>Under this bill, the DOJ must detain an individual who (1) is unlawfully present in the United States, made certain misrepresentations, or did not possess the necessary documents when applying for admission; and (2) has been charged with, arrested for, convicted of, or admits to having committed acts which constitute the essential elements of, an offense involving sexual assault.</p><p>The bill also establishes under statute that a conviction for certain crimes related to sexual assault shall be grounds for (1) barring an individual from entering the United States, and (2) deportability. (Under current law, convictions for certain crimes, including crimes involving moral turpitude, are grounds for inadmissibility and deportability.)\u00a0</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr134"
    },
    "title": "Protecting our Communities from Sexual Predators Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting our Communities from Sexual Predators Act</strong></p><p>This bill requires the Department of Justice (DOJ) to detain certain non-U.S. nationals (<em>aliens</em> under federal law) who have been arrested for sexual assault. The bill also provides for the inadmissibility and deportability of certain individuals convicted of sexual assault.</p><p>Under this bill, the DOJ must detain an individual who (1) is unlawfully present in the United States, made certain misrepresentations, or did not possess the necessary documents when applying for admission; and (2) has been charged with, arrested for, convicted of, or admits to having committed acts which constitute the essential elements of, an offense involving sexual assault.</p><p>The bill also establishes under statute that a conviction for certain crimes related to sexual assault shall be grounds for (1) barring an individual from entering the United States, and (2) deportability. (Under current law, convictions for certain crimes, including crimes involving moral turpitude, are grounds for inadmissibility and deportability.)\u00a0</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr134"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr134ih.xml"
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
      "title": "Protecting our Communities from Sexual Predators Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting our Communities from Sexual Predators Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to provide for the detention, inadmissibility, and removal of aliens who commit sexual assault.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T10:48:22Z"
    }
  ]
}
```

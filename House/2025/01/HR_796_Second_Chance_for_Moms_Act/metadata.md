# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/796?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/796
- Title: Second Chance for Moms Act
- Congress: 119
- Bill type: HR
- Bill number: 796
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-07-28T15:24:41Z
- Update date including text: 2025-07-28T15:24:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/796",
    "number": "796",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "Second Chance for Moms Act",
    "type": "HR",
    "updateDate": "2025-07-28T15:24:41Z",
    "updateDateIncludingText": "2025-07-28T15:24:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:10:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AL"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
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
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr796ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 796\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mrs. Miller of Illinois (for herself, Mr. Babin , Mr. Moore of Alabama , Mr. Moore of West Virginia , Mr. Ogles , Mr. Webster of Florida , Ms. Tenney , Mr. Clyde , Mr. Harris of Maryland , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to require a warning label advising that the effects of mifepristone can be counteracted, to amend the Public Health Service Act to establish a hotline to provide information to women seeking to counteract the effects of mifepristone, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Second Chance for Moms Act of 2025 .\n#### 2. Mifepristone warning label and hotline\n##### (a) Warning label\n**(1) In general**\nSection 502 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352 ) is amended by adding at the end the following:\n(hh) If it is the drug mifepristone, and its labeling does not bear the following statement printed in conspicuous text: WARNING: Medical evidence suggests that the abortifacient effects of mifepristone can be counteracted by natural progesterone, which can increase the chance of fetal survival. The American Society for Reproductive Medicine has determined that natural progesterone is safe in the first trimester of pregnancy. For more information, call [___]. (with the blank filled in to refer to the appropriate number for the hotline under section 1009 of the Public Health Service Act). .\n**(2) Effective date**\nSection 502(hh) of the Federal Food, Drug, and Cosmetic Act (as added by paragraph (1)) applies beginning on the date that is 6 months after the date of enactment of this Act.\n##### (b) Hotline\nTitle X of the Public Health Service Act ( 42 U.S.C. 300 et seq. ) is amended by adding at the end the following:\n1009. Hotline for reversal of effects of mifepristone (a) In general The Secretary shall establish or maintain, directly or by grant or contract, a toll-free hotline to provide support for 24 hours a day, 7 days a week, for women seeking to reverse the effects of the drug mifepristone. (b) Referrals to APR providers only A referral through the hotline described in subsection (a) may only be made to a health care provider that provides abortion pill reversal services. .",
      "versionDate": "2025-01-28",
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
            "name": "Abortion",
            "updateDate": "2025-03-27T15:47:27Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-03-27T15:47:45Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-03-27T15:47:34Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-03-27T15:47:37Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-03-27T15:47:49Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-03-27T15:47:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T14:53:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr796",
          "measure-number": "796",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr796v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Second Chance for Moms Act of 2025</strong></p><p>This bill requires labeling of the drug mifepristone to include certain information about the hormone progesterone and establishes a related telephone hotline. (Mifepristone is a drug that is approved to end pregnancies through 10 weeks gestation when used in conjunction with the drug misoprostol. The procedure is often referred to as medication abortion or the abortion pill.)</p>"
        },
        "title": "Second Chance for Moms Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr796.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Second Chance for Moms Act of 2025</strong></p><p>This bill requires labeling of the drug mifepristone to include certain information about the hormone progesterone and establishes a related telephone hotline. (Mifepristone is a drug that is approved to end pregnancies through 10 weeks gestation when used in conjunction with the drug misoprostol. The procedure is often referred to as medication abortion or the abortion pill.)</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr796"
    },
    "title": "Second Chance for Moms Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Second Chance for Moms Act of 2025</strong></p><p>This bill requires labeling of the drug mifepristone to include certain information about the hormone progesterone and establishes a related telephone hotline. (Mifepristone is a drug that is approved to end pregnancies through 10 weeks gestation when used in conjunction with the drug misoprostol. The procedure is often referred to as medication abortion or the abortion pill.)</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr796"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr796ih.xml"
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
      "title": "Second Chance for Moms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Chance for Moms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to require a warning label advising that the effects of mifepristone can be counteracted, to amend the Public Health Service Act to establish a hotline to provide information to women seeking to counteract the effects of mifepristone, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:29Z"
    }
  ]
}
```

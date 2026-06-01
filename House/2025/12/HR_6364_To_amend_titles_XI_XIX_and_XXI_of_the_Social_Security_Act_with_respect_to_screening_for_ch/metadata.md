# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6364?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6364
- Title: Kidd’s Stuttering Act
- Congress: 119
- Bill type: HR
- Bill number: 6364
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2026-05-22T08:08:42Z
- Update date including text: 2026-05-22T08:08:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6364",
    "number": "6364",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001240",
        "district": "6",
        "firstName": "Addison",
        "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
        "lastName": "McDowell",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Kidd\u2019s Stuttering Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:42Z",
    "updateDateIncludingText": "2026-05-22T08:08:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:00:25Z",
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
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "AL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "VA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "KY"
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
      "sponsorshipDate": "2025-12-15",
      "state": "TX"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "TN"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OH"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "UT"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "KY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NJ"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "NC"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6364ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6364\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. McDowell (for himself, Mr. Figures , and Mr. Vindman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend titles XI, XIX, and XXI of the Social Security Act with respect to screening for childhood onset fluency disorders, and to require coverage of certain speech therapy services under Medicaid and CHIP.\n#### 1. Short title\nThis Act may be cited as the Kidd\u2019s Stuttering Act .\n#### 2. Expanding screening and requiring coverage of certain speech therapy services under Medicaid and CHIP\n##### (a) Inclusion of screening for stuttering and speech fluency in core set of child health quality measures\nSection 1139A(b)(5) of the Social Security Act (42 U.S.C. 1320b\u20139a(b)(5)) is amended\u2014\n**(1)**\nby striking Beginning no later than and inserting the following:\n(A) In general Beginning no later than ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) Screening for stuttering and speech fluency (i) In general Not later than January 1, 2026, the Secretary shall publish changes to the core measures described in subsection (a) to include measures of screening for childhood-onset fluency disorders, including stuttering, for children who have attained the age of 2 (and have not attained the age of 6). (ii) Publication The Secretary shall publish the changes required by clause (i) at the same time and in the same manner as the relevant annual recommended changes required under subparagraph (A). .\n##### (b) Required screening for stuttering and speech fluency in Medicaid well-Child visits\nSection 1905(r)(1)(B) of the Social Security Act ( 42 U.S.C. 1396d(r)(1)(B) ) is amended\u2014\n**(1)**\nin clause (iv), by striking and at the end;\n**(2)**\nin clause (v), by striking the period at the end and inserting , and ; and\n**(3)**\nby adding at the end the following new clause:\n(vi) beginning January 1, 2027, for children who have attained the age of 2 (and have not attained the age of 6), screening for childhood-onset fluency disorders, including stuttering. .\n##### (c) Required coverage of certain speech therapy services\n**(1) Medicaid**\nTitle XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) is amended\u2014\n**(A)**\nin section 1902(a)\u2014\n**(i)**\nin paragraph (10)(A), by striking and (30) and inserting (30), and (32) ;\n**(ii)**\nin paragraph (88)(B)(iii), by striking and at the end;\n**(iii)**\nin paragraph (89), by striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following new paragraph:\n(90) provide that the treatment limitations applicable to specified speech therapy services (as defined in section 1905(ll)) are no more restrictive than the treatment limitations applicable to any speech therapy services for the treatment of expressive language disorder, receptive language disorder, mixed expressive and receptive language disorder, or articulation, for which medical assistance is provided under the State plan (or waiver of such plan). ; and\n**(B)**\nin section 1905\u2014\n**(i)**\nin subsection (a)\u2014\n**(I)**\nin paragraph (31), by striking and at the end;\n**(II)**\nby redesignating paragraph (32) as paragraph (33); and\n**(III)**\nby inserting after paragraph (31) the following new paragraph:\n(32) beginning on January 1, 2027, specified speech therapy services (as defined in subsection (ll)); and ; and\n**(ii)**\nby adding at the end the following new subsection:\n(ll) Specified speech therapy services For purposes of subsection (a)(32), the term specified speech therapy services \u2014 (1) means speech therapy services for the treatment of childhood-onset fluency disorders, including stuttering; and (2) includes such services delivered through real-time, audio and video telecommunications technology. .\n**(2) CHIP**\n**(A) In general**\nSection 2103(c) of the Social Security Act ( 42 U.S.C. 1397cc(c) ) is amended by adding at the end the following new paragraph:\n(13) Required coverage of certain speech therapy services Beginning January 1, 2027, the child health assistance provided to a targeted low-income child shall include coverage of specified speech therapy services (as such term is defined in section 1905(ll)). .\n**(B) Treatment parity**\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ) is amended\u2014\n**(i)**\nby redesignating subparagraphs (I) through (W) as subparagraphs (J) through (X), respectively; and\n**(ii)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) Section 1902(a)(90) (relating to parity in coverage of speech therapy services). .",
      "versionDate": "2025-12-02",
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
        "name": "Health",
        "updateDate": "2026-01-05T16:14:30Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6364ih.xml"
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
      "title": "To amend titles XI, XIX, and XXI of the Social Security Act with respect to screening for childhood onset fluency disorders, and to require coverage of certain speech therapy services under Medicaid and CHIP.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:28:13Z"
    },
    {
      "title": "Kidd\u2019s Stuttering Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kidd\u2019s Stuttering Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:20Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2512?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2512
- Title: EATS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2512
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-02-12T14:49:14Z
- Update date including text: 2026-02-12T14:49:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2512",
    "number": "2512",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "EATS Act of 2025",
    "type": "S",
    "updateDate": "2026-02-12T14:49:14Z",
    "updateDateIncludingText": "2026-02-12T14:49:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-07-29T19:55:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "OR"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NH"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2512is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2512\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mrs. Gillibrand (for herself, Mr. Fetterman , Mr. Merkley , Mr. Blumenthal , Ms. Slotkin , Mr. Sanders , Mr. Welch , Mr. Padilla , Mr. Booker , Mr. Wyden , Mrs. Shaheen , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to remove certain eligibility disqualifications that restrict otherwise eligible students from participating in the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhance Access To SNAP Act of 2025 or the EATS Act of 2025 .\n#### 2. Student eligibility under supplemental nutrition assistance program\n##### (a) Definition of household\nSection 3(m)(5) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(m)(5) ) is amended by adding at the end the following:\n(F) Individuals who are bona fide students enrolled at least half time in any recognized school, training program, or institution of higher education. .\n##### (b) Conditions of participation\nSection 6 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015 ) is amended\u2014\n**(1)**\nin subsection (d)(2)(C), by striking (except that any such person enrolled in an institution of higher education shall be ineligible to participate in the supplemental nutrition assistance program unless he or she meets the requirements of subsection (e) of this section) ;\n**(2)**\nby striking subsection (e); and\n**(3)**\nby redesignating subsections (f) through (s) as subsections (e) through (r), respectively.\n##### (c) Conforming amendments\n**(1)**\nSection 5 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014 ) is amended\u2014\n**(A)**\nin subsection (a), in the second sentence, by striking (g), and (r) and inserting (f), and (q) ; and\n**(B)**\nin subsection (i)(1), in the first sentence, by striking section 6(f)(2)(B) of this Act and inserting section 6(e)(2)(B) .\n**(2)**\nSection 6 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015 ) is amended\u2014\n**(A)**\nin subsection (d)(4)\u2014\n**(i)**\nin subparagraph (B)(ii)(I)(bb)(DD), by striking subsection (o) and inserting subsection (n) ; and\n**(ii)**\nin subparagraph (N), by striking subsection (o) each place it appears and inserting subsection (n) ; and\n**(B)**\nin paragraph (1)(B) of subsection (q) (as so redesignated), by striking subsection (k) and inserting subsection (j) .\n**(3)**\nSection 7(i)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(i)(1) ) is amended by striking section 6(o)(2) and inserting section 6(n)(2) .\n**(4)**\nSection 11 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020 ) is amended\u2014\n**(A)**\nin subsection (e)\u2014\n**(i)**\nin paragraph (2)(B)(v)(II), by striking section 6(f) and inserting section 6(e) ; and\n**(ii)**\nin paragraph (22), by striking section 6(i) and inserting section 6(h) ; and\n**(B)**\nin subsection (n), by striking section 6(g) and inserting section 6(f) .\n**(5)**\nSection 16(h) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025(h) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B)(ii), by striking section 6(o) and inserting section 6(n) ;\n**(ii)**\nin subparagraph (E)\u2014\n**(I)**\nby striking section 6(o)(3) each place it appears and inserting section 6(n)(3) ;\n**(II)**\nby striking section 6(o)(2) each place it appears and inserting section 6(n)(2) ; and\n**(III)**\nin clause (ii)\u2014\n**(aa)**\nin subclause (III), by striking section 6(o)(4) and inserting section 6(n)(4) ; and\n**(bb)**\nin subclause (IV), by striking section 6(o)(6) and inserting section 6(n)(6) ; and\n**(iii)**\nin subparagraph (F)(ii)(III)(ee)(AA), by striking section 6(o) and inserting section 6(n) ; and\n**(B)**\nin paragraph (5)(C)(iv)(I), by striking section 6(o)(2) and inserting section 6(n)(2) .\n**(6)**\nSection 17(m) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2026(m) ) is amended\u2014\n**(A)**\nby striking (l) through (n) each place it appears and inserting (k) through (m) ; and\n**(B)**\nin paragraph (2)(E), by striking section 6(l)(2) and inserting section 6(k)(2) .\n**(7)**\nSection 103(a)(2)(D) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3113(a)(2)(D) ) is amended by striking 6(o) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(o) ) and inserting 6(n) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(n) ) .\n**(8)**\nSection 121(b)(2)(B)(iv) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3151(b)(2)(B)(iv) ) is amended by striking 6(o) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(o) ) and inserting 6(n) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(n) ) .\n**(9)**\nSection 454 of the Social Security Act ( 42 U.S.C. 654 ) is amended\u2014\n**(A)**\nin paragraph (4)(A)(i)(IV), by striking 6(l)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(l)(1) ) and inserting 6(k)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(k)(1) ) ;\n**(B)**\nin paragraph (6)(B)(i), by striking subsection (l) or (m) of section 6 of the Food and Nutrition Act of 2008 and inserting subsection (k) or (l) of section 6 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015 ) ; and\n**(C)**\nin paragraph (29)(A)\u2014\n**(i)**\nby striking section 3(h) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(h) ) each place it appears and inserting section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ) ; and\n**(ii)**\nin clause (ii), by striking section 6(l)(2) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(l)(2) ) and inserting section 6(k)(2) of that Act ( 7 U.S.C. 2015(k)(2) ) .\n#### 3. Effective date\nThis Act and the amendments made by this Act shall take effect on January 2, 2026.",
      "versionDate": "2025-07-29",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-08-07T16:51:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
    "originChamber": "Senate",
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
          "measure-id": "id119s2512",
          "measure-number": "2512",
          "measure-type": "s",
          "orig-publish-date": "2025-07-29",
          "originChamber": "SENATE",
          "update-date": "2026-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2512v00",
            "update-date": "2026-02-12"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Enhance Access To SNAP Act of\u00a02025 or the EATS Act of 2025</strong></p><p>This bill expands eligibility for the Supplemental Nutrition Assistance Program (SNAP) for certain students.</p><p>Specifically, the bill removes the restriction on SNAP eligibility for students to allow otherwise eligible students who are attending institutions of higher education (IHEs) at least half time to participate in SNAP. Under current law, students 18-49 years old are restricted from participating in SNAP, with exceptions (e.g., caring for a child under the age of 6 or employed for at least 20 hours a week). The Consolidated Appropriations Act, 2021 temporarily exempted some students from certain SNAP eligibility requirements; these temporary student exemptions expired after the end of the COVID-19 public health emergency on May 11, 2023.</p><p>Further, the bill provides that students enrolled at least half time in a recognized school, training program, or IHE constitute individual <em>households</em> (not <em>residents of</em> <em>institutions</em>) and may be eligible for SNAP benefits. (Participation in SNAP is limited to households.)</p>"
        },
        "title": "EATS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2512.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Enhance Access To SNAP Act of\u00a02025 or the EATS Act of 2025</strong></p><p>This bill expands eligibility for the Supplemental Nutrition Assistance Program (SNAP) for certain students.</p><p>Specifically, the bill removes the restriction on SNAP eligibility for students to allow otherwise eligible students who are attending institutions of higher education (IHEs) at least half time to participate in SNAP. Under current law, students 18-49 years old are restricted from participating in SNAP, with exceptions (e.g., caring for a child under the age of 6 or employed for at least 20 hours a week). The Consolidated Appropriations Act, 2021 temporarily exempted some students from certain SNAP eligibility requirements; these temporary student exemptions expired after the end of the COVID-19 public health emergency on May 11, 2023.</p><p>Further, the bill provides that students enrolled at least half time in a recognized school, training program, or IHE constitute individual <em>households</em> (not <em>residents of</em> <em>institutions</em>) and may be eligible for SNAP benefits. (Participation in SNAP is limited to households.)</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119s2512"
    },
    "title": "EATS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Enhance Access To SNAP Act of\u00a02025 or the EATS Act of 2025</strong></p><p>This bill expands eligibility for the Supplemental Nutrition Assistance Program (SNAP) for certain students.</p><p>Specifically, the bill removes the restriction on SNAP eligibility for students to allow otherwise eligible students who are attending institutions of higher education (IHEs) at least half time to participate in SNAP. Under current law, students 18-49 years old are restricted from participating in SNAP, with exceptions (e.g., caring for a child under the age of 6 or employed for at least 20 hours a week). The Consolidated Appropriations Act, 2021 temporarily exempted some students from certain SNAP eligibility requirements; these temporary student exemptions expired after the end of the COVID-19 public health emergency on May 11, 2023.</p><p>Further, the bill provides that students enrolled at least half time in a recognized school, training program, or IHE constitute individual <em>households</em> (not <em>residents of</em> <em>institutions</em>) and may be eligible for SNAP benefits. (Participation in SNAP is limited to households.)</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119s2512"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2512is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "EATS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EATS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Enhance Access To SNAP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to remove certain eligibility disqualifications that restrict otherwise eligible students from participating in the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:21Z"
    }
  ]
}
```

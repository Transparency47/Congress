# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/343?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/343
- Title: Keep Our PACT Act
- Congress: 119
- Bill type: S
- Bill number: 343
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2026-01-14T16:09:09Z
- Update date including text: 2026-01-14T16:09:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/343",
    "number": "343",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Keep Our PACT Act",
    "type": "S",
    "updateDate": "2026-01-14T16:09:09Z",
    "updateDateIncludingText": "2026-01-14T16:09:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
          "date": "2025-01-30T22:11:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "HI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "RI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "MA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-30",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "OR"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "MN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "NM"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "MN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "IL"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "MA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CO"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MD"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "NM"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "NH"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NJ"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "DE"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s343is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 343\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Van Hollen (for himself, Mr. Padilla , Ms. Hirono , Mr. Reed , Mr. Murphy , Mr. Markey , Mr. Blumenthal , Mr. Sanders , Mr. Merkley , Mr. Durbin , Mr. Booker , Ms. Klobuchar , Mr. Heinrich , Ms. Smith , Ms. Duckworth , Ms. Warren , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require full funding of part A of title I of the Elementary and Secondary Education Act of 1965 and the Individuals with Disabilities Education Act.\n#### 1. Short title\nThis Act may be cited as the Keep Our Promise to America\u2019s Children and Teachers Act or the Keep Our PACT Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nChildren are our Nation\u2019s future and greatest treasure.\n**(2)**\nA high-quality education is the surest way for every child to reach his or her full potential.\n**(3)**\nPart A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ) helps address inequity in education in school districts across the United States to provide a high-quality education to every student.\n**(4)**\nThe Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ) guarantees all children with disabilities a first-rate education.\n**(5)**\nThe amendments made to such Act by the Individuals with Disabilities Education Improvement Act of 2004 ( Public Law 108\u2013446 ; 118 Stat. 2647) committed Congress to providing 40 percent of the national current average per-pupil expenditure for students with disabilities.\n**(6)**\nA promise made must be a promise kept.\n#### 3. Mandatory funding of part A of title I of ESEA\n##### (a) Definition of fiscal year 2025 part A of title I appropriation\nIn this section, the term fiscal year 2025 part A of title I appropriation means the amount appropriated for fiscal year 2025 for programs under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ).\n##### (b) Funding\nThere are appropriated, out of any money in the Treasury not otherwise appropriated\u2014\n**(1)**\nfor fiscal year 2026, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$20,509,878,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(2)**\nfor fiscal year 2027, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$22,853,242,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(3)**\nfor fiscal year 2028, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$25,464,349,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(4)**\nfor fiscal year 2029, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$28,373,788,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(5)**\nfor fiscal year 2030, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$31,615,646,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(6)**\nfor fiscal year 2031, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$35,227,904,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(7)**\nfor fiscal year 2032, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$39,252,882,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(8)**\nfor fiscal year 2033, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$43,737,735,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(9)**\nfor fiscal year 2034, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$48,735,007,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater; and\n**(10)**\nfor fiscal year 2035, $54,303,244,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater.\n#### 4. Mandatory funding of the Individuals With Disabilities Education Act\nSection 611(i) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1411(i) ) is amended to read as follows:\n(i) Funding (1) In general For the purpose of carrying out this part, other than section 619, there are authorized to be appropriated\u2014 (A) $16,661,928,000 or 11.6 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2026, and there are hereby appropriated $6,425,048,000 or 4.5 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2026, which shall become available for obligation on July 1, 2026, and shall remain available through September 30, 2027; (B) $19,531,844,000 or 13.4 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2027, and there are hereby appropriated $8,372,932,000 or 5.7 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2027, which shall become available for obligation on July 1, 2027, and shall remain available through September 30, 2028; (C) $22,896,084,000 or 15.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2028, and there are hereby appropriated $10,911,357,000 or 7.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2028, which shall become available for obligation on July 1, 2028, and shall remain available through September 30, 2029; (D) $26,839,795,000 or 17.6 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2029, and there are hereby appropriated $14,219,357,000 or 9.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2029, which shall become available for obligation on July 1, 2029, and shall remain available through September 30, 2030; (E) $31,462,786,000 or 20.2 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2030, and there are hereby appropriated $18,530,244,000 or 11.9 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2030, which shall become available for obligation on July 1, 2030, and shall remain available through September 30, 2031; (F) $36,882,058,000 or 23.1 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2031, and there are hereby appropriated $24,148,064,000 or 15.2 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2031, which shall become available for obligation on July 1, 2031, and shall remain available through September 30, 2032; (G) $43,234,768,000 or 26.5 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2032, and there are hereby appropriated $31,469,041,000 or 19.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2032, which shall become available for obligation on July 1, 2032, and shall remain available through September 30, 2033; (H) $50,681,693,000 or 30.4 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2033, and there are hereby appropriated $41,009,521,000 or 24.6 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2033, which shall become available for obligation on July 1, 2033, and shall remain available through September 30, 2034; (I) $59,411,305,000 or 34.9 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2034, and there are hereby appropriated $53,442,392,000 or 31.4 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2034, which shall become available for obligation on July 1, 2034, and shall remain available through September 30, 2035; and (J) $69,644,540,000 or 40 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2035 and each subsequent fiscal year, and there are hereby appropriated $69,644,540,000 or 40 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2035 and each subsequent fiscal year, which\u2014 (i) shall become available for obligation with respect to fiscal year 2035 on July 1, 2034, and shall remain available through September 30, 2036; and (ii) shall become available for obligation with respect to each subsequent fiscal year on July 1 of that fiscal year and shall remain available through September 30 of the succeeding fiscal year. (2) Amount With respect to each subparagraph of paragraph (1), the amount determined under this paragraph is the product of\u2014 (A) the total number of children with disabilities in all States who\u2014 (i) received special education and related services during the last school year that concluded before the first day of the fiscal year for which the determination is made; and (ii) were aged\u2014 (I) 3 through 5 (with respect to the States that were eligible for grants under section 619); and (II) 6 through 21; and (B) the average per-pupil expenditure in public elementary schools and secondary schools in the United States. .\n#### 5. Emergency designation\n##### (a) In general\nThe amounts provided by the amendments made by this Act are designated as an emergency requirement pursuant to section 4(g) of the Statutory Pay-As-You-Go Act of 2010 ( 2 U.S.C. 933(g) ).\n##### (b) Designation in house and senate\nThe amendments made by this Act are designated as being for an emergency requirement pursuant to section 4001(a)(1) of S. Con. Res. 14 (117th Congress), the concurrent resolution on the budget for fiscal year 2022, and to legislation establishing fiscal year 2026 through 2035 budget enforcement in the House of Representatives.",
      "versionDate": "2025-01-30",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-31",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "869",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Keep Our PACT Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-02",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2598",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "IDEA Full Funding Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1277",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "IDEA Full Funding Act",
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
            "name": "Appropriations",
            "updateDate": "2025-03-24T16:05:41Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-24T16:05:41Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-24T16:05:41Z"
          },
          {
            "name": "Special education",
            "updateDate": "2025-03-24T16:05:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-07T16:03:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s343",
          "measure-number": "343",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s343v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Keep Our Promise to America's Children and Teachers Act or the Keep Our PACT Act </strong></p><p>This bill provides funding through FY2035 for grant programs operated by local educational agencies to provide supplementary educational and related services to low-achieving students and other students who attend elementary and secondary schools with relatively high concentrations of students from low-income families. Additionally, the bill permanently reauthorizes the grant program to assist states and outlying areas in providing special education and related services to children with disabilities.</p><p>The amounts provided by the bill are designated as an emergency requirement for the purposes of Pay-As-You-Go (PAYGO) rules and other budget enforcement procedures.\u00a0</p>"
        },
        "title": "Keep Our PACT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s343.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep Our Promise to America's Children and Teachers Act or the Keep Our PACT Act </strong></p><p>This bill provides funding through FY2035 for grant programs operated by local educational agencies to provide supplementary educational and related services to low-achieving students and other students who attend elementary and secondary schools with relatively high concentrations of students from low-income families. Additionally, the bill permanently reauthorizes the grant program to assist states and outlying areas in providing special education and related services to children with disabilities.</p><p>The amounts provided by the bill are designated as an emergency requirement for the purposes of Pay-As-You-Go (PAYGO) rules and other budget enforcement procedures.\u00a0</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s343"
    },
    "title": "Keep Our PACT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep Our Promise to America's Children and Teachers Act or the Keep Our PACT Act </strong></p><p>This bill provides funding through FY2035 for grant programs operated by local educational agencies to provide supplementary educational and related services to low-achieving students and other students who attend elementary and secondary schools with relatively high concentrations of students from low-income families. Additionally, the bill permanently reauthorizes the grant program to assist states and outlying areas in providing special education and related services to children with disabilities.</p><p>The amounts provided by the bill are designated as an emergency requirement for the purposes of Pay-As-You-Go (PAYGO) rules and other budget enforcement procedures.\u00a0</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s343"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s343is.xml"
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
      "title": "Keep Our PACT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep Our PACT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep Our Promise to America\u2019s Children and Teachers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require full funding of part A of title I of the Elementary and Secondary Education Act of 1965 and the Individuals with Disabilities Education Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:32Z"
    }
  ]
}
```

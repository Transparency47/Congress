# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2541?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2541
- Title: Food Date Labeling Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2541
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-03-20T11:03:18Z
- Update date including text: 2026-03-20T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2541",
    "number": "2541",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Food Date Labeling Act of 2025",
    "type": "S",
    "updateDate": "2026-03-20T11:03:18Z",
    "updateDateIncludingText": "2026-03-20T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
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
      "actionDate": "2025-07-30",
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
        "item": [
          {
            "date": "2025-07-30T18:12:00Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-30T18:12:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "FL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "DE"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2541is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2541\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Blumenthal (for himself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish requirements for quality and discard date phrases that are voluntarily declared on the food label to display calendar dates.\n#### 1. Short title\nThis Act may be cited as the Food Date Labeling Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administering Secretaries**\nThe term administering Secretaries means\u2014\n**(A)**\nthe Secretary of Agriculture, with respect to any product that is\u2014\n**(i)**\nunder the jurisdiction of the Secretary of Agriculture; and\n**(ii)**\n**(I)**\na poultry product (as defined in section 4 of the Poultry Products Inspection Act ( 21 U.S.C. 453 ));\n**(II)**\na meat food product (as defined in section 1 of the Federal Meat Inspection Act ( 21 U.S.C. 601 )); or\n**(III)**\nan egg product (as defined in section 4 of the Egg Products Inspection Act ( 21 U.S.C. 1033 )); and\n**(B)**\nthe Secretary of Health and Human Services, with respect to any product that is\u2014\n**(i)**\nunder the jurisdiction of the Secretary of Health and Human Services; and\n**(ii)**\na food (as defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )).\n**(2) Discard date phrase**\nThe term discard date phrase means a phrase voluntarily printed on a food packaging that signifies the end of the estimated period of shelf life under any stated storage conditions, after which the entity responsible for the food label advises the product not be consumed.\n**(3) Quality date phrase**\nThe term quality date phrase means a phrase voluntarily printed on a food packaging that is intended to communicate to consumers when\u2014\n**(A)**\nthe quality of the product may begin to deteriorate; but\n**(B)**\nthe product remains apparently wholesome food (as defined in subsection (b) of the Bill Emerson Good Samaritan Food Donation Act ( 42 U.S.C. 1791(b) )).\n#### 3. Quality date phrases and discard date phrases\n##### (a) Quality date phrases\n**(1) In general**\nIf a quality date is used on a food package, such quality date shall be proceeded by the uniform quality date label phrase under paragraph (2).\n**(2) Uniform phrase**\nThe uniform quality date label phrase under this paragraph shall be BEST If Used By or, if permissible under subsection (c)(3), the standard abbreviation of BB , unless and until the administering Secretaries, acting in coordination, specify through rulemaking another uniform phrase to be used for purposes of complying with paragraph (1).\n**(3) Option of the entity responsible for the food label**\nThe decisions of whether to include a quality date or quality date phrase on food packaging and which foods should be so labeled shall be at the discretion of the entity responsible for the food label.\n##### (b) Discard date phrases\n**(1) In general**\nIf a discard date is used on food packaging, such discard date shall be proceeded by the uniform discard date label phrase under paragraph (2).\n**(2) Uniform phrase**\nThe uniform discard date label phrase under this paragraph shall be USE By or, if permissible under subsection (c)(3), the standard abbreviation of UB , unless and until the administering Secretaries, acting in coordination, specify through rulemaking another uniform phrase to be used for purposes of complying with paragraph (1).\n**(3) Option of the entity responsible for the food label**\nThe decisions of whether to include a discard date or discard date phrase on food packaging and which foods should be so labeled shall be at the discretion of the entity responsible for the food label.\n##### (c) Quality date phrase and discard date phrase labeling\n**(1) In general**\nThe quality date or discard date, as applicable, shall be\u2014\n**(A)**\nin single easy-to-read type style; and\n**(B)**\nlocated in a conspicuous and prominent place on the food label or elsewhere on the package.\n**(2) Date format**\nThe format of each quality date and discard date that follows the quality date phrase and discard date phrase, as applicable, shall be stated in terms of month and year or, as appropriate, month, day, and year.\n**(3) Abbreviations**\nA standard abbreviation of BB and UB for the quality date phrase and discard date phrase, respectively, may be used only if the food packaging is too small to include the uniform phrase described in subsection (a)(2) or (b)(2), as applicable.\n**(4) Use of technologies and additional labels**\nThe labeling required under this subsection may utilize time-temperature indicator labels, QR codes, smart labels, or similar technology, in addition to any uniform quality date label phrase under subsection (a)(2) or uniform discard label phrase under subsection (b)(2). Nothing in this Act or an amendment made by this Act prohibits or restricts the use of such technology or labeling in lieu of any uniform quality date label phrase under subsection (a)(2) or uniform discard date label phrase under subsection (b)(2).\n**(5) Freeze by**\nThe entity responsible for the food label may add or freeze by following a uniform quality date label phrase or discard date label phrase.\n##### (d) Education\nNot later than 2 years after the date of enactment of this Act, the administering Secretaries, acting in coordination, shall provide consumer education and outreach on the meaning of quality date phrases and discard date phrases on food packaging.\n##### (e) Effect; preemption\n**(1) Effect on sale or donation of foods**\nNothing in this Act or an amendment made by this Act prohibits any State or political subdivision of a State from establishing or continuing in effect any requirement that prohibits the sale or donation of foods based on passage of the discard date.\n**(2) Effect on infant formula**\nNothing in this Act or an amendment made by this Act\u2014\n**(A)**\napplies with respect to infant formula (as defined in section 201(z) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(z) )); or\n**(B)**\naffects the requirements relating to infant formula under section 412 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a ) or any other applicable provision of law.\n**(3) Preemption**\nNo State or political subdivision of a State may establish or continue in effect any requirement that\u2014\n**(A)**\nrelates to the inclusion in food labeling of a quality date phrase or a discard date phrase that is different from, in addition to, or otherwise not identical with, the requirements of this Act and the amendments made by this Act; or\n**(B)**\nprohibits the sale or donation of foods based on passage of the quality date.\n**(4) Enforcement**\nThe administering Secretaries, in consultation with the Federal Trade Commission, shall ensure that the uniform quality date label phrase and uniform discard date label phrase are standardized across all food products.\n**(5) Savings provision**\nNotwithstanding paragraph (3), nothing in this Act, any amendment made by this Act, or any standard or requirement imposed pursuant to this Act preempts, displaces, or supplants any State or Federal common law rights or any State or Federal statute creating a remedy for civil relief, including under the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(6) Rule of construction**\nNothing in this subsection shall be construed to\u2014\n**(A)**\nauthorize the Secretary of Health and Human Services to require that a food be labeled for quality standards or for a discard date as described in subsections (a) and (b); or\n**(B)**\npreempt a State from setting requirements for a quality date or discard date or a timeline of quality, listed on a food label, provided that the requirement complies with the uniform quality data phrase or discard date phrase specified in subsection (a)(2) or (b)(2).\n#### 4. Misbranding\n##### (a) FDA violations\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) If the label bears a quality date phrase or discard date phrase that fails to comply with the requirements as specified in sections 3(a) and 3(b) of the Food Date Labeling Act of 2025 , or that fails to meet the requirements as specified in section 3(c) of such Act. .\n##### (b) Poultry products\nSection 4(h) of the Poultry Products Inspection Act ( 21 U.S.C. 453(h) ) is amended\u2014\n**(1)**\nin paragraph (11), by striking or at the end;\n**(2)**\nin paragraph (12), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(13) if its labeling is in violation of section 3 of the Food Date Labeling Act of 2025 . .\n##### (c) Meat products\nSection 1(n) of the Federal Meat Inspection Act ( 21 U.S.C. 601(n) ) is amended\u2014\n**(1)**\nin paragraph (11), by striking or at the end;\n**(2)**\nin paragraph (12), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(13) if its labeling is in violation of section 3 of the Food Date Labeling Act of 2025 . .\n##### (d) Egg products\nSection 7(b) of the Egg Products Inspection Act ( 21 U.S.C. 1036(b) ) is amended in the first sentence by inserting or if its labeling is in violation of section 3 of the Food Date Labeling Act of 2025 before the period at the end.\n#### 5. Regulations\nNot later than 2 years after the date of enactment of this Act, the administering Secretaries, in coordination with each other, shall promulgate final regulations for carrying out this Act.\n#### 6. Delayed applicability\nThis Act and the amendments made by this Act shall apply only with respect to food products that are labeled on or after the date that is 2 years after the date of enactment of this Act.",
      "versionDate": "2025-07-30",
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
        "actionDate": "2025-08-15",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4987",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Food Date Labeling Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-05T17:22:30Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2541is.xml"
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
      "title": "Food Date Labeling Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Food Date Labeling Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish requirements for quality and discard date phrases that are voluntarily declared on the food label to display calendar dates.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:18Z"
    }
  ]
}
```

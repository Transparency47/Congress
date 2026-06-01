# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1012
- Title: SOIL Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1012
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-05-13T11:03:31Z
- Update date including text: 2026-05-13T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1012",
    "number": "1012",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "SOIL Act of 2025",
    "type": "S",
    "updateDate": "2026-05-13T11:03:31Z",
    "updateDateIncludingText": "2026-05-13T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
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
      "actionDate": "2025-03-12",
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
            "date": "2025-03-12T22:39:44Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-12T22:39:44Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ID"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1012is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1012\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Lankford (for himself, Mr. Bennet , Mr. Risch , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo increase oversight of foreign direct investment in agricultural land in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Security and Oversight for International Landholdings Act of 2025 or the SOIL Act of 2025 .\n#### 2. Review by Committee on Foreign Investment in the United States of certain agricultural real estate transactions\nSection 721(a)(4) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking ; and and inserting a semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) any transaction described in clause (vi) or (vii) of subparagraph (B) proposed or pending on or after the date of the enactment of this clause. ; and\n**(2)**\nin subparagraph (B), by adding at the end the following:\n(vi) Any acquisition or transfer of an interest, other than a security, in agricultural land held by a person that is a national of, or is organized under the laws or otherwise subject to the jurisdiction of, a country\u2014 (I) designated as a nonmarket economy country pursuant to section 771(18) of the Tariff Act of 1930 ( 19 U.S.C. 1677(18) ); or (II) identified as a country that poses as risk to the national security of the United States in the most recent annual report on worldwide threats issued by the Director of National Intelligence pursuant to section 108B of the National Security Act of 1947 ( 50 U.S.C. 3043b )(commonly known as the Annual Threat Assessment ). .\n#### 3. Review by Committee on Foreign Investment in the United States of real estate transactions near military installations\nSection 721(a)(4)(B) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(4)(B) ), as amended by section 2, is amended by adding at the end the following:\n(vii) Any acquisition or transfer of an interest, other than a security, in any form of real estate that is located not more than 50 miles from a military installation (as that term is defined in section 2801(c)(4) of title 10, United States Code) other than residential property held by a person that is a national of, or is organized under the laws or otherwise subject to the jurisdiction of, a country\u2014 (I) designated as a nonmarket economy country pursuant to section 771(18) of the Tariff Act of 1930 ( 19 U.S.C. 1677(18) ); or (II) identified as a country that poses as risk to the national security of the United States in the most recent annual report on worldwide threats issued by the Director of National Intelligence pursuant to section 108B of the National Security Act of 1947 ( 50 U.S.C. 3043b )(commonly known as the Annual Threat Assessment ). .\n#### 4. Prohibition on use of funds for certain agricultural real estate holdings\nNo assistance, including subsidies, may be provided by any Federal agency to a person for an agricultural real estate holding wholly or partly owned by a person that is a national of, or is organized under the laws or otherwise subject to the jurisdiction of, a country\u2014\n**(1)**\ndesignated as a nonmarket economy country pursuant to section 771(18) of the Tariff Act of 1930 ( 19 U.S.C. 1677(18) ); or\n**(2)**\nidentified as a country that poses as risk to the national security of the United States in the most recent annual report on worldwide threats issued by the Director of National Intelligence pursuant to section 108B of the National Security Act of 1947 ( 50 U.S.C. 3043b )(commonly known as the Annual Threat Assessment ).\n#### 5. Disclosure requirements for foreign agricultural real estate holdings\n##### (a) Reporting requirements\nSection 2(a) of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501(a) ) is amended\u2014\n**(1)**\nin the first sentence of the matter preceding paragraph (1)\u2014\n**(A)**\nby inserting , or enters into a leasing agreement the period of which is longer than 5 years with respect to agricultural land, after agricultural land ; and\n**(B)**\nby striking acquisition or transfer and inserting acquisition, transfer, or lease ; and\n**(2)**\nin paragraph (4), by striking acquired or transferred and inserting acquired, transferred, or leased .\n##### (b) Revocation of minimum acreage requirement\nSection 9(1) of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3508(1) ) is amended by inserting , subject to the condition that the Secretary may not exclude land from this definition based on the acreage of the land before the semicolon at the end.\n#### 6. Reports of holdings of agricultural land in the United States by foreign persons\nSection 6 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3505 ) is amended\u2014\n**(1)**\nby striking the section designation and heading and all that follows through Not later than and inserting the following:\n6. Reports (a) Transmission of reports to States Not later than ; and\n**(2)**\nby adding at the end the following:\n(b) Annual report (1) In general Annually, the Secretary shall prepare and make publicly available a report describing holdings of agricultural land by foreign persons, as determined by reports submitted under section 2, including\u2014 (A) an analysis of the countries with the most extensive agricultural land holdings on a State-by-State and county-by-county basis; (B) data and an analysis of agricultural land holdings in each county in the United States by a foreign person from\u2014 (i) the People\u2019s Republic of China; (ii) the Russian Federation; or (iii) any other country that the Secretary determines to be appropriate; and (C) an analysis of the sectors and industries for which the agricultural land holdings are used. (2) Transmission to States The Secretary shall transmit the report prepared under paragraph (1) to each State department of agriculture or appropriate State agency described in subsection (a) in conjunction with the applicable reports transmitted under that subsection. .",
      "versionDate": "2025-03-12",
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
        "updateDate": "2025-05-20T23:09:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s1012",
          "measure-number": "1012",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1012v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Security and Oversight for International Landholdings Act of 2025 or the SOIL Act of 2025</strong></p><p>This bill establishes and expands requirements for reviewing and disclosing transactions regarding foreign investments in agricultural land.</p><p>The Committee on Foreign Investment in the United States (CFIUS) must review certain investments in agricultural land held by a person (i.e., individual or entity) that is a national of, or subject to the jurisdiction of, a country (1) designated as a nonmarket economy, or (2) identified as posing a risk to the national security of the United States. Under current law, CFIUS reviews the national security implications of certain foreign investments in U.S. businesses or real estate, including critical infrastructure or technologies.</p><p>CFIUS must also review certain real estate acquisitions or transfers of an interest, other than a security, for nonresidential properties that are located within 50 miles of a military installation.</p><p>The bill also prohibits federal assistance, including subsidies, from being provided to a person for an agricultural real estate holding which is owned by any of the foreign persons specified above.</p><p>The bill requires any foreign person who enters into a leasing agreement for agricultural land that is longer than five years to report the lease to the Department of Agriculture (USDA). Current requirements only apply to agriculture land acquired or transferred.</p><p>Further, USDA must prepare and make publicly available an annual report describing agricultural land holdings by foreign persons, including specific information related to foreign persons from China and Russia.</p>"
        },
        "title": "SOIL Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1012.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Security and Oversight for International Landholdings Act of 2025 or the SOIL Act of 2025</strong></p><p>This bill establishes and expands requirements for reviewing and disclosing transactions regarding foreign investments in agricultural land.</p><p>The Committee on Foreign Investment in the United States (CFIUS) must review certain investments in agricultural land held by a person (i.e., individual or entity) that is a national of, or subject to the jurisdiction of, a country (1) designated as a nonmarket economy, or (2) identified as posing a risk to the national security of the United States. Under current law, CFIUS reviews the national security implications of certain foreign investments in U.S. businesses or real estate, including critical infrastructure or technologies.</p><p>CFIUS must also review certain real estate acquisitions or transfers of an interest, other than a security, for nonresidential properties that are located within 50 miles of a military installation.</p><p>The bill also prohibits federal assistance, including subsidies, from being provided to a person for an agricultural real estate holding which is owned by any of the foreign persons specified above.</p><p>The bill requires any foreign person who enters into a leasing agreement for agricultural land that is longer than five years to report the lease to the Department of Agriculture (USDA). Current requirements only apply to agriculture land acquired or transferred.</p><p>Further, USDA must prepare and make publicly available an annual report describing agricultural land holdings by foreign persons, including specific information related to foreign persons from China and Russia.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s1012"
    },
    "title": "SOIL Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Security and Oversight for International Landholdings Act of 2025 or the SOIL Act of 2025</strong></p><p>This bill establishes and expands requirements for reviewing and disclosing transactions regarding foreign investments in agricultural land.</p><p>The Committee on Foreign Investment in the United States (CFIUS) must review certain investments in agricultural land held by a person (i.e., individual or entity) that is a national of, or subject to the jurisdiction of, a country (1) designated as a nonmarket economy, or (2) identified as posing a risk to the national security of the United States. Under current law, CFIUS reviews the national security implications of certain foreign investments in U.S. businesses or real estate, including critical infrastructure or technologies.</p><p>CFIUS must also review certain real estate acquisitions or transfers of an interest, other than a security, for nonresidential properties that are located within 50 miles of a military installation.</p><p>The bill also prohibits federal assistance, including subsidies, from being provided to a person for an agricultural real estate holding which is owned by any of the foreign persons specified above.</p><p>The bill requires any foreign person who enters into a leasing agreement for agricultural land that is longer than five years to report the lease to the Department of Agriculture (USDA). Current requirements only apply to agriculture land acquired or transferred.</p><p>Further, USDA must prepare and make publicly available an annual report describing agricultural land holdings by foreign persons, including specific information related to foreign persons from China and Russia.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s1012"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1012is.xml"
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
      "title": "SOIL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SOIL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Security and Oversight for International Landholdings Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase oversight of foreign direct investment in agricultural land in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:20Z"
    }
  ]
}
```

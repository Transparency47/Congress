# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1919?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1919
- Title: Buying American Cotton Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1919
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1919",
    "number": "1919",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Buying American Cotton Act of 2025",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
            "date": "2025-05-22T20:27:08Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T20:27:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "AL"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "KS"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "AR"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "NC"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "AL"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "TX"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "TN"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AR"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MO"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "SC"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "KS"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1919is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1919\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mrs. Hyde-Smith (for herself, Mrs. Britt , Mr. Marshall , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a domestic cotton consumption credit.\n#### 1. Short title\nThis Act may be cited as the Buying American Cotton Act of 2025 .\n#### 2. Domestic cotton consumption credit\n##### (a) Purpose\nThe purposes of this section are\u2014\n**(1)**\nto encourage the consumption of cotton which originated in the United States, and products which are made from such cotton, and\n**(2)**\nto document the processing of such cotton through a trustworthy supply chain tracing system.\n##### (b) Allowance of credit\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Domestic cotton consumption credit (a) Credit allowed For purposes of section 38, the domestic cotton consumption credit determined under this section for any taxable year is an amount equal to the product of\u2014 (1) the documented volume of qualified cotton in an eligible article sold by the taxpayer in a qualifying sale during the taxable year, (2) the applicable percentage, and (3) the applicable cotton market price. (b) Qualifying sale; applicable percentage; applicable cotton market price (1) Qualifying sale For purposes of this section\u2014 (A) In general The term qualifying sale means, with respect to any eligible article, the first sale of such eligible article to an unrelated person. (B) Exception Such term shall not include any sale for use or consumption of an eligible article outside of the United States unless such sale results in income which is effectively connected with a trade or business in the United States. (C) Related persons Persons shall be treated as related to each other if such persons would be treated as a single employer under the regulations prescribed under section 52(b). (2) Applicable percentage For purposes of subsection (a)(2), the applicable percentage is\u2014 (A) in the case of an eligible article consisting of qualified cotton that\u2014 (i) was only subject to processing in the United States, or (ii) in addition to any processing that may have occurred within the United States, was subject to additional processing only in a country or countries with which the United States has entered into a free trade agreement or for which the United States has extended benefits through a unilateral preference program, 24 percent, and (B) in the case of an eligible article consisting of qualified cotton that was subject to additional processing at any stage of its processing in a country with which the United States has not entered into a free trade agreement or for which the United States has not extended benefits through a unilateral preference program, 18 percent. (3) Applicable cotton market price For purposes of this section, the term applicable cotton market price means, with respect to any eligible article, the average market price for qualified cotton in a recognized international market (as determined by the Secretary, in consultation with the Secretary of Agriculture) for the 3-calendar year period ending with or within the taxable year immediately preceding the taxable year in which the eligible article is sold. (c) Other definitions For purposes of this section\u2014 (1) Eligible article (A) In general The term eligible article means any product which\u2014 (i) is comprised in whole or in part of qualified cotton which is certified, under such regulations established by the Secretary in consultation with the Secretary of Agriculture, as meeting the requirements of paragraph (2)(B)(ii), (ii) is in its final condition, and (iii) is ready for retail sale to a consumer. (B) Exception Such term shall not include any product if\u2014 (i) any component of such product is an eligible article for which a credit has been allowed, or (ii) the taxpayer selling such product has been notified by the person from whom such a component was acquired that such person intended to claim such credit. (C) Final condition (i) In general For purposes of subparagraph (A)(ii), the term final condition means, with respect to any article, the physical state in which such article is presented for sale or sold for immediate resale to a consumer, determined\u2014 (I) without regard to any de minimis augmentation that could be performed on it by or on behalf of a retailer of the eligible article, and (II) without regard to packaging. (ii) De minimis augmentation For purposes of clause (i)(I), the term de minimis augmentation means any graphics or other adornment imposed on or attached to the article. (2) Qualified cotton (A) In general The term qualified cotton means extra long staple cotton (as defined in section 1111 of the Agricultural Act of 2014) or upland cotton (within the meaning of section 1207(c) of such Act) which\u2014 (i) is grown in the United States, and (ii) meets the proof of origin requirements of subparagraph (B). (B) Proof of origin requirements Cotton meets the proof of origin requirements of this subparagraph if\u2014 (i) such cotton was\u2014 (I) assigned a permanent bale identification number, or (II) meets such other requirements as the Secretary, in consultation with the Secretary of Agriculture, determines is sufficient to prove that the cotton originated in the United States, and (ii) the movement and volume of such cotton is digitally traced, under such regulations established by the Secretary in consultation with the Secretary of Agriculture, through the supply chain from its United States origin through to the last stage of processing into an eligible article. (C) Permanent bale identification number The term permanent bale identification number means the autogenerated identification number assigned by the Secretary of Agriculture to a bale of qualified cotton that was grown and ginned in the United States. (3) Free trade agreement (A) In general Except as provided by subparagraph (B), the term free trade agreement means a comprehensive bilateral or regional agreement\u2014 (i) that covers substantially all trade between the parties to the agreement, and (ii) with respect to which an implementing bill (as defined in section 151 of the Trade Act of 1974 ( 19 U.S.C. 2191 )) is enacted into law. (B) Exclusions The term free trade agreement does not include\u2014 (i) the WTO Agreement, as defined in section 2 of the Uruguay Round Agreements Act ( 19 U.S.C. 3501 ), (ii) the agreements specified in 101(d) of that Act ( 19 U.S.C. 3511(d) ), or (iii) any other multilateral agreement of the World Trade Organization or any successor entity. (4) Unilateral preference program (A) In general Except as provided by subparagraph (B), the term unilateral preference program \u2014 (i) means a program of the United States that provides preferential duty treatment to textile or apparel articles imported from a foreign country that is designated as a beneficiary of the program, and (ii) includes\u2014 (I) the African Growth and Opportunity Act ( 19 U.S.C. 3701 et seq. ) and section 506A of the Trade Act of 1974 ( 19 U.S.C. 2466a ), (II) the Caribbean Basin Economic Recovery Act ( 19 U.S.C. 2701 et seq. ), (III) section 915 of the Trade Facilitation and Trade Enforcement Act of 2015 ( 19 U.S.C. 4454 ), and (IV) any other provision of law\u2014 (aa) establishing a program that provides preferential duty treatment to textile or apparel articles imported from a foreign country that is designated as a beneficiary of the program, and (bb) that is enacted after the date of the enactment of this section. (B) Exclusion The term unilateral preference program does not include the Generalized System of Preferences under title V of the Trade Act of 1974 ( 19 U.S.C. 2461 et seq. ). (5) Processing (A) In general The term processing means any physical process, or any stage in such process, that contributes to the conversion of an item comprised in whole or in part of qualified cotton into an eligible article. (B) Exception Such term shall not include the mere physical possession, storage, movement, or packaging of cotton or any eligible article. (6) United States The term United States includes any possessions of the United States. (7) Volume The term volume means, with respect to any eligible article, the amount of qualified cotton in such article, as measured in pounds. (d) Increased credit for qualified cotton yarn and qualified cotton fabric (1) Qualified cotton yarn (A) In general At the election of the taxpayer, in the case of any eligible article which is composed in whole or in part of qualified cotton yarn\u2014 (i) this section shall be applied separately with respect to such cotton yarn, and (ii) the amount determined under subsection (a) with respect to such cotton yarn shall be equal to such amount (determined without regard to this subsection) multiplied by 1.6. (B) Qualified cotton yarn For purposes of this subsection, the term qualified cotton yarn means a strand of fiber made in the United States from qualified cotton into a form suitable for weaving, knitting, braiding, felting, webbing, or otherwise fabricating into a fabric. (2) Qualified cotton fabric (A) In general At the election of the taxpayer, in the case of any eligible article which is composed in whole or in part of qualified cotton fabric\u2014 (i) this section shall be applied separately with respect to such cotton fabric, and (ii) the amount determined under subsection (a) with respect to such cotton fabric shall be equal to such amount (determined without regard to this subsection) multiplied by 6.5. (B) Qualified cotton fabric For purposes of this subsection, the term qualified cotton fabric means any material woven, knitted, felted, or otherwise produced in the United States from, or in combination with, any fiber, yarn, or substitute thereof that was made in the United States from qualified cotton. (3) Election An election under this subsection shall be made at such time and in such form as the Secretary may be regulations provide. (e) Regulations The Secretary shall prescribe such regulations and other guidance as may be necessary or appropriate to carry out this section, including regulations or guidance\u2014 (1) to establish a system for preventing the credit allowed under this subsection more than once with respect to any amount of qualified cotton, which may include establishing a requirement to notify purchasers of eligible articles of the intent to claim the credit allowed under this section, (2) with respect to the digital tracing of cotton under subsection (c)(2)(B)(ii), which may include requirements to identify the taxpayers within the supply chain, and (3) with respect to the certification of qualified cotton under subsection (c)(1)(A)(i), which may require reporting of the specific volume of qualified cotton in the eligible article. .\n##### (c) Credit allowed as part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41), and by adding at the end the following new paragraph:\n(42) the domestic cotton consumption credit determined under section 45BB. .\n##### (d) Transfer of credit\nSection 6418(f)(1)(A) of such Code is amended by adding at the end the following:\n(xii) The domestic cotton consumption credit determined under section 45BB(a). .\n##### (e) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following item:\nSec. 45BB. Domestic cotton consumption credit. .\n##### (f) Effective date\nThe amendments made by this section shall apply to eligible articles (as defined in section 45BB of the Internal Revenue Code of 1986, as added by subsection (b)) that are sold on or after January 20, 2025.",
      "versionDate": "2025-05-22",
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
        "actionDate": "2026-01-22",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7230",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Buying American Cotton Act of 2026",
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
        "name": "Taxation",
        "updateDate": "2025-06-23T17:45:19Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1919is.xml"
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
      "title": "Buying American Cotton Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Buying American Cotton Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a domestic cotton consumption credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:50Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4255?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4255
- Title: Expedited Disability Insurance Payments for Terminally Ill Individuals Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4255
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-13T13:46:23Z
- Update date including text: 2026-04-13T13:46:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4255",
    "number": "4255",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Expedited Disability Insurance Payments for Terminally Ill Individuals Act of 2026",
    "type": "S",
    "updateDate": "2026-04-13T13:46:23Z",
    "updateDateIncludingText": "2026-04-13T13:46:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T20:46:51Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NH"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "WY"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "DE"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AK"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4255is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4255\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Barrasso (for himself, Ms. Hassan , Ms. Lummis , Mr. Coons , Ms. Murkowski , and Mr. Reed ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for phased-in payment of Social Security Disability Insurance payments during the waiting period for individuals with a terminal illness.\n#### 1. Short title\nThis Act may be cited as the Expedited Disability Insurance Payments for Terminally Ill Individuals Act of 2026 .\n#### 2. Phased-in payment of SSDI benefits during the waiting period for the terminally ill\n##### (a) In general\nSection 223 of the Social Security Act ( 42 U.S.C. 423 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), in the matter following subparagraph (E), by striking or (iii) and inserting (iii) subject to paragraph (2)(B), for each month beginning with the first month during all of which the individual is determined under subparagraph (D) of subsection (d)(2) to be under a disability and in which he becomes so entitled to such insurance benefits, or (iv) ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking section 202(q) and and inserting paragraph (3) of this subsection, section 202(q), and ;\n**(ii)**\nin subparagraph (A), by striking or at the end; and\n**(iii)**\nin subparagraph (B), by striking clause (ii) of paragraph (1) and inserting clause (ii), (iii), or (iv) in the matter following subparagraph (E) of paragraph (1) ; and\n**(C)**\nby adding at the end the following new paragraph:\n(3) (A) For purposes of paragraph (2), in any case in which clause (iii) in the matter following subparagraph (E) of paragraph (1) of this subsection is applicable to an individual, the amount of the individual's monthly disability insurance benefit for the earliest period of 2 consecutive calendar months throughout which the individual has been entitled to such insurance benefits shall be equal to the product of the benefit amount determined for the individual under paragraph (2) (before application of this paragraph) and\u2014 (i) for the first calendar month, 50 percent; and (ii) for the second calendar month, 75 percent. (B) If an individual who has been determined under subparagraph (D) of subsection (d)(2) to be under a disability has been entitled to a disability insurance benefit on such basis for 12 consecutive calendar months, the individual's disability insurance benefit for any month during the subsequent period of 12 consecutive calendar months shall be equal to\u2014 (i) the benefit amount determined for the individual under paragraph (2) (before application of this paragraph); minus (ii) the quotient obtained by dividing the total amount of disability insurance benefits provided to the individual during the earliest period of five consecutive calendar months for which the individual was entitled to such benefits on such basis by 12. (C) If an individual who has been determined under subparagraph (D) of subsection (d)(2) to be under a disability has been entitled to a disability insurance benefit on such basis for 24 consecutive calendar months, the individual's disability insurance benefit for any subsequent month shall be equal to 95 percent of the benefit amount determined for the individual under paragraph (2) (before application of this paragraph). ; and\n**(2)**\nin subsection (d)(2), by adding at the end the following:\n(D) For purposes of clause (iii) in the matter following subparagraph (E) of paragraph (1) of subsection (a), an individual shall be determined to be under a disability upon submission of a diagnosis of a terminal illness (as defined in section 1861(dd)(3)(A)) that has been certified by not less than 2 physicians (as defined in section 1861(r)(1)) who are not related (as described in section 267(c)(4) of the Internal Revenue Code of 1986) and are not in the same physician group practice. .\n##### (b) Reports to Congress\n**(1) Report by Social Security Administration**\nNot later than 1 year after the date of the enactment of this Act, and each year thereafter, the Commissioner of the Social Security Administration, in coordination with the Inspector General of the Social Security Administration, shall submit to the relevant committees of Congress a report that evaluates the provision of disability insurance benefits to terminally ill individuals, including\u2014\n**(A)**\nthe total number of individuals who\u2014\n**(i)**\nfile applications for disability insurance benefits (as determined under section 223(a)(3) of the Social Security Act) based on a diagnosis of a terminal illness;\n**(ii)**\nreceive such benefits;\n**(iii)**\ndie within 6 months of first receiving such benefits;\n**(iv)**\ndie within 12 months of first receiving such benefits;\n**(v)**\nreceive such benefits during the period described in section 223(a)(3)(B) of the Social Security Act; and\n**(vi)**\nreceive such benefits during the period described in section 223(a)(3)(C) of the Social Security Act;\n**(B)**\nthe total amount expended, including related administrative expenses, for the provision of disability insurance benefits under section 223(a)(3) of the Social Security Act to individuals diagnosed with a terminal illness; and\n**(C)**\nrecommendations for such legislation and administrative actions as are determined appropriate for preventing fraud, waste, and abuse related to such benefits.\n**(2) Report by Government Accountability Office**\nNot later than 2 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit a report to the relevant committees of Congress that evaluates the provision of disability insurance benefits to terminally ill individuals and provides recommendations for such legislation and administrative actions as are determined appropriate to improve the provision of such benefits to such individuals.\n##### (c) Effective date\nThe amendments made by this section shall apply to benefits payable for months beginning after December 31, 2026.",
      "versionDate": "2026-03-26",
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
        "name": "Social Welfare",
        "updateDate": "2026-04-13T13:46:23Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4255is.xml"
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
      "title": "Expedited Disability Insurance Payments for Terminally Ill Individuals Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T02:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expedited Disability Insurance Payments for Terminally Ill Individuals Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for phased-in payment of Social Security Disability Insurance payments during the waiting period for individuals with a terminal illness.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:03:21Z"
    }
  ]
}
```

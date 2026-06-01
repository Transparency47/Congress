# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8536
- Title: Fuel STAR Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8536
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-19T20:24:56Z
- Update date including text: 2026-05-19T20:24:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8536",
    "number": "8536",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Fuel STAR Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-19T20:24:56Z",
    "updateDateIncludingText": "2026-05-19T20:24:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
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
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:03:30Z",
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
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "WI"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8536ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8536\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mr. Arrington (for himself and Mr. Moran ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to reform the Renewable Fuel Standard, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fuel and Strengthen the American Refinery Act of 2026 or the Fuel STAR Act of 2026 .\n#### 2. Renewable Fuel Standard reforms\n##### (a) In general\nSection 211(o) of the Clean Air Act ( 42 U.S.C. 7545(o) ) is amended\u2014\n**(1)**\nin paragraph (2)(B), by adding at the end the following:\n(vi) Maximum changes in applicable volumes Notwithstanding clauses (iii) through (v) and the analyses required under subclauses (I) through (VI) of clause (ii), for the purpose of making the determinations in clause (ii), the Administrator shall ensure that, for the first calendar year that begins after the date of enactment of this clause and for each calendar year thereafter, the applicable volume for renewable fuel that is not advanced biofuel does not exceed the projected annual domestic consumption of ethanol blended fuel projected in the most recent Annual Energy Outlook report of the Energy Information Administration for the applicable year. ;\n**(2)**\nin paragraph (5)\u2014\n**(A)**\nin subparagraph (C), by striking A credit and inserting Except as provided in subparagraph (F), a credit ; and\n**(B)**\nby adding at the end the following:\n(F) Extended duration of certain credits A credit generated under this paragraph in calendar year 2020 through 2022 may be used to show compliance for any of the 5 calendar years following the date of the enactment of this subparagraph, except that not more than 20 percent of the credits used by a person to demonstrate compliance with paragraph (2) in a calendar year may be credits that were generated in calendar year 2020 through 2022. (G) Prohibition In promulgating regulations under paragraph (2)(A) to carry out this paragraph, the Administrator may not impose a requirement to use an electric credit (commonly referred to as an e-RIN ). ; and\n**(3)**\nin paragraph (9)\u2014\n**(A)**\nin subparagraph (A), by adding at the end the following:\n(iii) Applicability to certain small refineries (I) In general A small refinery described in subclause (III) is eligible to receive an exemption from compliance with the requirements of paragraph (2) with respect to a calendar year for the reason of disproportionate economic hardship. (II) Treatment The Administrator shall deem any exemption under this clause as an extension of an exemption under subparagraph (A), and the requirements of subparagraphs (B), (C), and (D) shall apply in the same manner and to the same extent with respect to such exemptions as to such extensions of exemptions. (III) Small refineries described A small refinery described in this subclause is a small refinery\u2014 (aa) for which the average aggregate daily crude oil throughput for a calendar year (as determined by dividing the aggregate throughput for the calendar year by the number of days in the calendar year) does not exceed 10,000 barrels; and (bb) that began production on or after January 1, 2007. ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking the exemption and inserting an exemption ;\n**(ii)**\nin clause (ii), by inserting after and other economic factors.\nBeginning on date that is 1 year after the date of enactment of the Farm, Food, and National Security Act of 2026, such economic factors shall be the following: (I) As applicable to small refineries under the control of a holding company, the cost of credits purchased by such holding company to demonstrate compliance with paragraph (2) calendar year divided by the revenue of such holding company over the calendar year. (II) Whether the costs to a small refinery of complying with the requirements of paragraph (2) would eliminate efficiency gains, as described in the study of the Department of Energy titled Small Refinery Exemption Study An Investigation into Disproportionate Economic Hardship and dated March 2011. (III) Whether the costs to a small refinery of complying with such requirements are likely to lead to the refinery ceasing to operate. (IV) Exceptional State regulatory environment, as determined by the Administrator. (V) Whether a small refinery is actively building infrastructure to blend biofuels, as demonstrated by the submission of a plan to the Administrator. ;\n**(iii)**\nin clause (iii)\u2014\n**(I)**\nby striking The Administrator and inserting the following:\n(I) In general The Administrator ; and\n**(II)**\nby adding at the end the following:\n(II) Failure to respond If the Administrator does not, during the 90-day period described in subclause (I), provide to the petitioner a description of the legal basis pursuant to which the Administrator has determined that the small refinery that is the subject of the petition under clause (i) does not qualify for an extension of an exemption under subparagraph (A), the petition shall be considered granted. ; and\n**(iv)**\nby adding at the end the following:\n(iv) Approval of certain petitions Notwithstanding clause (ii) and subject to clause (v), the Administrator shall grant a petition submitted under clause (i) by a small refinery for an extension of an exemption under subparagraph (A) if the Secretary of Energy determines that, with respect to the small refinery\u2014 (I) the disproportionate impacts index, as described in the report of the Office of Policy and International Affairs of the Department of Energy entitled Small Refinery Exemption Study: An Investigation into Disproportionate Economic Hardship and dated March 2011, is greater than or equal to 1; or (II) the viability index, as described in the report described in subclause (I), is greater than or equal to 1. (v) Limitation The Administrator may not approve a petition submitted under clause (i) by a small refinery under the control of a holding company if such approval would result in a total exempted volume that\u2014 (I) taken together with any other refinery under the control of the holding company, exceeds 75,000 barrels of oil produced per day or 50 percent of the total amount of barrels of oil produced per day by such refineries, whichever is greater; or (II) exceeds the combined total capacity for barrels of oil produced per day by any small refinery under such control. ; and\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nby striking If a small and inserting the following:\n(i) Effect of waiver If a small ; and\n**(ii)**\nby adding at the end the following:\n(ii) Effect of exemption If the Administrator grants a petition for an extension of an exemption under subparagraph (A) submitted by a small refinery, the Administrator may not reallocate the renewable fuel obligation of that small refinery to other refineries. .\n##### (b) Year-Round sale of E15\nSection 211 of the Clean Air Act ( 42 U.S.C. 7545 ) is further amended\u2014\n**(1)**\nin subsection (f), by adding at the end the following:\n(6) The Reid vapor pressure limitation applicable under this subsection to fuel blends containing gasoline and a percent of denatured anhydrous ethanol that exceeds 10 percent and is not more than 15 percent shall be the same as any such limitation applicable under this subsection to fuel blends containing gasoline and 10 percent denatured anhydrous ethanol. ; and\n**(2)**\nin subsection (h)\u2014\n**(A)**\nin paragraph (4), by striking 10 percent and inserting 10 to 15 percent ; and\n**(B)**\nin paragraph (5)(A), by striking 10 percent and inserting 10 to 15 percent .",
      "versionDate": "2026-04-28",
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
        "name": "Energy",
        "updateDate": "2026-05-19T20:24:56Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8536ih.xml"
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
      "title": "Fuel STAR Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fuel STAR Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fuel and Strengthen the American Refinery Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Clean Air Act to reform the Renewable Fuel Standard, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:36Z"
    }
  ]
}
```

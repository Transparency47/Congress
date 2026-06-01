# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7384
- Title: Preventing Mass Casualties from Release of Hydrofluoric Acid at Refineries Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7384
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-18T16:02:42Z
- Update date including text: 2026-02-18T16:02:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7384",
    "number": "7384",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Preventing Mass Casualties from Release of Hydrofluoric Acid at Refineries Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-18T16:02:42Z",
    "updateDateIncludingText": "2026-02-18T16:02:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:04:30Z",
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
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7384ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7384\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. Waters (for herself, Mr. Lieu , Ms. Barrag\u00e1n , Mr. Garcia of California , Ms. Tlaib , Ms. Norton , and Mr. Cohen ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Toxic Substances Control Act to prohibit the use of hydrogen fluoride (hydrofluoric acid) at petroleum refineries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Mass Casualties from Release of Hydrofluoric Acid at Refineries Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nHydrogen fluoride (hydrofluoric acid) is an exceptionally hazardous chemical, which is used in large quantities in approximately 40 petroleum refineries in the United States to refine petroleum in order to produce high octane gasoline.\n**(2)**\nPetroleum refineries are vulnerable to accidents, natural disasters, and intentional subversive acts, which could result in the release of a large quantity of hydrogen fluoride (hydrofluoric acid).\n**(3)**\nThe release of a sufficient quantity of hydrogen fluoride (hydrofluoric acid) from a petroleum refinery has in the past, and could in the future, caused immediate injuries or deaths to refinery workers who are exposed.\n**(4)**\nThe release of a sufficient quantity of hydrogen fluoride (hydrofluoric acid) from a petroleum refinery could cause a mass casualty event in the surrounding community, resulting in immediate deaths or permanent injuries to thousands of people living, working, or traveling within a radius of up to 25 miles.\n**(5)**\nMore than 14 million people are at risk of death or permanent injuries as a result of living in communities surrounding petroleum refineries that use hydrogen fluoride (hydrofluoric acid), and many of these at-risk communities are disproportionately impacted by environmental burdens.\n**(6)**\nAlternative technologies are available that would enable petroleum refineries to convert from the use of hydrogen fluoride (hydrofluoric acid) to a vastly safer, commercially proven alternative method for refining petroleum to produce high octane gasoline, and these alternative technologies are already used in the majority of refineries in the United States.\n**(7)**\nNew petroleum refineries should not be allowed to use hydrogen fluoride (hydrofluoric acid) to refine petroleum, and petroleum refineries that currently use hydrogen fluoride (hydrofluoric acid) should be required to convert to a safer alternative.\n#### 3. Prohibition on use of hydrofluoric acid at petroleum refineries\nSection 6 of the Toxic Substances Control Act ( 15 U.S.C. 2605 ) is amended\u2014\n**(1)**\nby redesignating subsection (j) as subsection (k); and\n**(2)**\nby inserting after subsection (i) the following:\n(j) Prohibition on use of hydrofluoric acid at petroleum refineries (1) New refineries No person may use hydrogen fluoride (hydrofluoric acid) to refine petroleum at a petroleum refinery that begins operating on or after the date of enactment of this subsection. (2) Existing refineries (A) Prohibition Beginning on the date that is 5 years after the date of enactment of this subsection, no person may use hydrogen fluoride (hydrofluoric acid) to refine petroleum at a petroleum refinery that began operating before the date of enactment of this subsection. (B) Civil penalty Notwithstanding the first sentence of section 16(a)(1), the amount of a civil penalty under such first sentence for violating a provision of section 15 with respect to a requirement of this paragraph shall be $37,500 for each such violation. (3) Application of waiver authority Notwithstanding section 22, the Administrator may not issue a waiver under such section with respect to the prohibition on the use of hydrogen fluoride (hydrofluoric acid) at a petroleum refinery under this subsection. .",
      "versionDate": "2026-02-04",
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
        "name": "Environmental Protection",
        "updateDate": "2026-02-18T16:02:42Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7384ih.xml"
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
      "title": "Preventing Mass Casualties from Release of Hydrofluoric Acid at Refineries Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T04:43:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Mass Casualties from Release of Hydrofluoric Acid at Refineries Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-13T04:43:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Toxic Substances Control Act to prohibit the use of hydrogen fluoride (hydrofluoric acid) at petroleum refineries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T04:18:35Z"
    }
  ]
}
```

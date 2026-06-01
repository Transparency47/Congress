# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4732?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4732
- Title: Orphanage Trafficking Prevention and Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 4732
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-10-04T08:06:05Z
- Update date including text: 2025-10-04T08:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4732",
    "number": "4732",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Orphanage Trafficking Prevention and Protection Act",
    "type": "HR",
    "updateDate": "2025-10-04T08:06:05Z",
    "updateDateIncludingText": "2025-10-04T08:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:18:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MD"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4732ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4732\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Smith of New Jersey (for himself, Mr. Mfume , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo expand the definition of severe forms of trafficking in persons to include the recruitment, harboring, transportation, transfer, or receipt of orphaned, abandoned, or minors living in public or private residential facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Orphanage Trafficking Prevention and Protection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOrphaned, abandoned, and children living in public or private residential facilities, including institutions, children\u2019s homes, orphanages, boarding schools, or group homes, are among the populations most vulnerable to trafficking in persons worldwide. According to the United States Department of State, children without parental care are at significantly higher risk of being trafficked for labor, sexual exploitation, forced begging, and other illegal purposes.\n**(2)**\nAn estimated 5,400,000 children live in institutional care globally, many of whom are not true orphans but are separated from their families due to poverty, disability, or family breakdown.\n**(3)**\nTraffickers often target these children under the guise of education, caregiving, or adoption.\n**(4)**\nThe Department of State\u2019s 2024 Trafficking in Persons Report notes that orphanage trafficking \u2014the recruitment of children into residential care for the purpose of exploitation and profit\u2014occurs in multiple countries and is increasingly linked to international travel, and volun-tourism.\n**(5)**\nThe Department of State\u2019s 2019 and 2024 Trafficking in Persons Reports have identified patterns in which children are trafficked into orphanages to attract donations and international volunteers, with reports of physical, emotional, and sexual abuse in such institutions.\n**(6)**\nIn some cases, children are fraudulently labeled as orphans and trafficked through inter-country adoption channels, undermining legitimate adoption systems and violating the Convention on Protection of Children and Co-operation in Respect of Intercountry Adoption, done at the Hague on May 29, 1993.\n**(7)**\nDespite these documented abuses, current United States law does not explicitly recognize orphanage trafficking as a severe form of trafficking in persons, which, accordingly, may hinder efforts to prosecute perpetrators, protect victims, and condition foreign assistance.\n**(8)**\nClarifying that the trafficking of orphaned, abandoned, or children living in public or private residential facilities, including institutions, children\u2019s homes, orphanages, boarding schools, or group homes, constitutes a severe form of trafficking in persons under the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7101 et seq. ) is necessary to protect these children, enhance accountability, and strengthen United States anti-trafficking efforts.\n#### 3. Modification to definition of severe forms of trafficking in persons\nParagraph (11) of section 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking ; or at the end and inserting a semicolon;\n**(2)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) the recruitment, harboring, transportation, transfer, or receipt of orphaned, abandoned, or persons living in public or private residential facilities who have not attained 18 years of age, by means of fraud, coercion, force, or abuse of a position of vulnerability, for the purpose of exploitation and profit, forced labor, involuntary servitude, peonage, debt bondage, slavery, child labor, or sex trafficking. .",
      "versionDate": "2025-07-23",
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
        "name": "International Affairs",
        "updateDate": "2025-09-11T17:27:33Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4732ih.xml"
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
      "title": "Orphanage Trafficking Prevention and Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Orphanage Trafficking Prevention and Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand the definition of \"severe forms of trafficking in persons\" to include the recruitment, harboring, transportation, transfer, or receipt of orphaned, abandoned, or minors living in public or private residential facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:28Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5158?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5158
- Title: Fair Price Device Act
- Congress: 119
- Bill type: HR
- Bill number: 5158
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2025-09-22T15:51:44Z
- Update date including text: 2025-09-22T15:51:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5158",
    "number": "5158",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Fair Price Device Act",
    "type": "HR",
    "updateDate": "2025-09-22T15:51:44Z",
    "updateDateIncludingText": "2025-09-22T15:51:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:02:25Z",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5158ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5158\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Ms. Scholten introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act regarding the approval of combination products consisting of a generic drug and a device, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Price Device Act .\n#### 2. Generic drugs for use with devices\nSection 505(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j) ) is amended\u2014\n**(1)**\nin paragraph (2)(A)\u2014\n**(A)**\nin clause (v)\u2014\n**(i)**\nby striking except for changes required because of differences and inserting except for changes required or appropriate, as determined by the Secretary, because of differences ; and\n**(ii)**\nby inserting , including changes as a result of differences that are otherwise permitted under this subsection, such as changes as a result of appropriate differences in the device for use with the new drug before the semicolon;\n**(B)**\nin clause (vii), by striking the and at the end;\n**(C)**\nin clause (viii) by striking the period at the end and inserting ; and ;\n**(D)**\nby inserting after clause (viii) the following new clause:\n(ix) if the listed drug referred to in clause (i) is intended for use with a device, relevant information as determined by the Secretary to support that the new drug for use with the device can be expected to have the same clinical effect and safety profile as the listed drug for use with the device when administered to patients under the conditions specified in the labeling of the drug, which information\u2014 (I) shall be in addition to information under clauses (i) through (viii) that is relevant, as determined by the Secretary, to the evaluation of the new drug for use with the device and the device proposed for use with the new drug; and (II) may include\u2014 (aa) information (comparative and non-comparative) regarding the device and its performance, including information about the compatibility of the new drug with the device and information regarding the delivery of the new drug when used with the device; (bb) comparative analyses of the new drug for use with the device and the listed drug for use with its device, including information identifying any differences between the user interface of the new drug and listed drug; information identifying any differences between the user interface of the device proposed for use with the new drug and the device used with the listed drug; and information to show that, despite any such differences, the new drug when used with the device can be expected to have the same clinical effect and safety profile as the listed drug when used with the device when administered to patients under the conditions specified in the labeling of the drug; and (cc) comparative and non-comparative human factors studies. ; and\n**(E)**\nin the matter following clause (ix), as inserted by subparagraph (D), by striking through (viii) and inserting through (ix) ; and\n**(2)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (G)\u2014\n**(i)**\nby striking except for changes required because of differences and inserting except for changes required or appropriate, as determined by the Secretary, because of differences ; and\n**(ii)**\nby inserting , including changes as a result of differences that are otherwise permitted under this subsection, such as changes as a result of appropriate differences in the device for use with the new drug before the semicolon;\n**(B)**\nby redesignating subparagraphs (J) through (K) as subparagraphs (K) through (L); and\n**(C)**\nby inserting after subparagraph (I) the following:\n(J) if the listed drug is intended for use with a device, information submitted in the application is insufficient to show that the new drug for use with the device can be expected to have the same clinical effect and safety profile as the listed drug for use with the device when administered to patients under the conditions specified in the labeling of the drug; .",
      "versionDate": "2025-09-04",
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
        "updateDate": "2025-09-22T15:51:44Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5158ih.xml"
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
      "title": "Fair Price Device Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Price Device Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act regarding the approval of combination products consisting of a generic drug and a device, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:23Z"
    }
  ]
}
```

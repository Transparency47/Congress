# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2608?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2608
- Title: To remove certain species from the lists of threatened species and endangered species published pursuant to the Endangered Species Act of 1973.
- Congress: 119
- Bill type: HR
- Bill number: 2608
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2025-10-09T03:26:19Z
- Update date including text: 2025-10-09T03:26:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2608",
    "number": "2608",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To remove certain species from the lists of threatened species and endangered species published pursuant to the Endangered Species Act of 1973.",
    "type": "HR",
    "updateDate": "2025-10-09T03:26:19Z",
    "updateDateIncludingText": "2025-10-09T03:26:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2608ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2608\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Roy (for himself and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo remove certain species from the lists of threatened species and endangered species published pursuant to the Endangered Species Act of 1973.\n#### 1. Removal of certain species from lists of threatened species and endangered species\n##### (a) In general\nNotwithstanding any other provision of law, the following species are removed from the lists of threatened species and endangered species, as applicable, that are published pursuant to section 4 of the Endangered Species Act of 1973 ( 16 U.S.C. 1533 ):\n**(1)**\nArabian oryx (Oryx leucoryx).\n**(2)**\nBanteng (Bos javanicus).\n**(3)**\nEld\u2019s brow-antlered deer (Cervus eldi).\n**(4)**\nGrevy\u2019s zebra (Equus grevyi).\n**(5)**\nRed lechwe (Kobus leche).\n**(6)**\nSeledang (Bos gaurus).\n**(7)**\nSwamp deer (Cervus duvauceli).\n##### (b) Bukharan markhor\nSection 4(a) of the Endangered Species Act of 1973 ( 16 U.S.C. 1533(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking The Secretary shall by regulation and inserting Except as provided in paragraph (4), the Secretary shall by regulation ; and\n**(2)**\nby adding at the end the following:\n(4) Applicability to Bukharan markhor The Secretary may not make a determination under this subsection that the Bukharan markhor (Capra falconeri heptneri) is a threatened species or an endangered species. .",
      "versionDate": "2025-04-02",
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
        "name": "Animals",
        "updateDate": "2025-04-08T16:35:51Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2608ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To remove certain species from the lists of threatened species and endangered species published pursuant to the Endangered Species Act of 1973.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T11:18:23Z"
    },
    {
      "title": "To remove certain species from the lists of threatened species and endangered species published pursuant to the Endangered Species Act of 1973.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:39Z"
    }
  ]
}
```

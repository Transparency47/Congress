# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/921?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/921
- Title: Recognizing the 30th anniversary of the Dayton Peace Accords.
- Congress: 119
- Bill type: HRES
- Bill number: 921
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2025-12-03T21:26:45Z
- Update date including text: 2025-12-03T21:26:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-02 - IntroReferral: Submitted in House
- 2025-12-02 - IntroReferral: Submitted in House
- Latest action: 2025-12-02: Submitted in House

## Actions

- 2025-12-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-02 - IntroReferral: Submitted in House
- 2025-12-02 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/921",
    "number": "921",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000463",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. Turner, Michael R. [R-OH-10]",
        "lastName": "Turner",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Recognizing the 30th anniversary of the Dayton Peace Accords.",
    "type": "HRES",
    "updateDate": "2025-12-03T21:26:45Z",
    "updateDateIncludingText": "2025-12-03T21:26:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
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
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-12-02T15:01:10Z",
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
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "MO"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MO"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres921ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 921\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Turner of Ohio (for himself, Mrs. Wagner , Mr. Bell , and Mr. Guthrie ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing the 30th anniversary of the Dayton Peace Accords.\nThat the House of Representatives\u2014\n**(1)**\nreaffirms the joint United States and EU commitment to promote and protect human rights, democracy, and the rule of law in Bosnia and Herzegovina and around the world;\n**(2)**\ncommends the continued commitment of the people of Bosnia and Herzegovina to peace and cooperation 30 years after the Dayton Peace Accords;\n**(3)**\nnotes the efforts undertaken by the Government of Bosnia and Herzegovina toward NATO and EU membership, including measures to resolve its constitutional issues, strengthen its governing structures, and undertake necessary economic, rule of law, and judicial reforms;\n**(4)**\nreiterates the continued importance of the Dayton Peace Accords as the basis of constitutional reform in Bosnia and Herzegovina and the promotion of political, economic, legal, and religious equality, which are also key requirements for EU accession;\n**(5)**\nurges the Government of Bosnia and Herzegovina to continue to pursue constitutional reforms needed to reconcile the past and engage across ethnic and religious lines with empathy and respect to build a common future;\n**(6)**\nurges the Government of Bosnia and Herzegovina, through its respective leaders, to uphold the integrity of the tripartite presidency, strengthen its key institutions, and work to achieve an independent democracy;\n**(7)**\nurges the United States Government to maintain support for the Office of the High Representative until members of the Peace Implementation Council reach a unanimous agreement that the presence of the Office of the High Representative is no longer necessary;\n**(8)**\nurges the United States Government to work closely with Bosnia and Herzegovina and its bordering nations\u2014especially those who are signatories of the Dayton Peace Accords\u2014to support full implementation of the Stabilization and Association Agreement between the EU and the Balkan States;\n**(9)**\nencourages continued regional cooperation to combat the malign influence of foreign actors, such as the Russian Federation and the People\u2019s Republic of China;\n**(10)**\nrecognizes the State of Ohio and the greater Dayton community for their role in fostering the Dayton Peace Accords, and for continuing to support diplomacy, security, and peace around the world; and\n**(11)**\nacknowledges the important contributions of the Bosnian-American diaspora in their communities throughout the United States.",
      "versionDate": "2025-12-02",
      "versionType": "IH"
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
        "updateDate": "2025-12-03T21:26:45Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres921ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Recognizing the 30th anniversary of the Dayton Peace Accords.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T09:18:31Z"
    },
    {
      "title": "Recognizing the 30th anniversary of the Dayton Peace Accords.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T09:06:11Z"
    }
  ]
}
```

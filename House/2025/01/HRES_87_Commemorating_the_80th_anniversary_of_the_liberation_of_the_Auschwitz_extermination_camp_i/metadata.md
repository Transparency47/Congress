# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/87?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/87
- Title: Commemorating the 80th anniversary of the liberation of the Auschwitz extermination camp in Nazi-occupied Poland and International Holocaust Remembrance Day.
- Congress: 119
- Bill type: HRES
- Bill number: 87
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-03-07T16:42:36Z
- Update date including text: 2025-03-07T16:42:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-31 - Committee: Submitted in House
- Latest action: 2025-01-31: Submitted in House

## Actions

- 2025-01-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-31 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/87",
    "number": "87",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Commemorating the 80th anniversary of the liberation of the Auschwitz extermination camp in Nazi-occupied Poland and International Holocaust Remembrance Day.",
    "type": "HRES",
    "updateDate": "2025-03-07T16:42:36Z",
    "updateDateIncludingText": "2025-03-07T16:42:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionCode": "H12100",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-31T15:00:50Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres87ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 87\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. Meng (for herself, Mr. Lawler , Ms. Lois Frankel of Florida , and Mr. Bacon ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nCommemorating the 80th anniversary of the liberation of the Auschwitz extermination camp in Nazi-occupied Poland and International Holocaust Remembrance Day.\nThat the House of Representatives\u2014\n**(1)**\ncalls on all people of the United States to remember the 1,100,000 innocent victims murdered at the Auschwitz extermination camp as part of the Holocaust, the 6,000,000 Jews killed during the Holocaust, and all of the victims of the Nazi reign of terror;\n**(2)**\nhonors the legacy of the survivors of the Holocaust and of the Auschwitz extermination camp;\n**(3)**\ncalls on the people of the United States to continue to work toward tolerance, peace, and justice and to continue to work to end all genocide and persecution; and\n**(4)**\nrecommits to combating all forms of anti-Semitism.",
      "versionDate": "2025-01-31",
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
        "updateDate": "2025-02-20T14:55:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
    "originChamber": "House",
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
          "measure-id": "id119hres87",
          "measure-number": "87",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres87v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution calls on the people of the United States to remember the innocent victims murdered at Auschwitz, the Jews killed during the Holocaust, and all the victims of the Nazi reign of terror.\u00a0The resolution also (1) calls on the people of the United States to continue working to end all genocide and persecution, and (2) recommits to combating all forms of anti-Semitism.</p>"
        },
        "title": "Commemorating the 80th anniversary of the liberation of the Auschwitz extermination camp in Nazi-occupied Poland and International Holocaust Remembrance Day."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres87.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution calls on the people of the United States to remember the innocent victims murdered at Auschwitz, the Jews killed during the Holocaust, and all the victims of the Nazi reign of terror.\u00a0The resolution also (1) calls on the people of the United States to continue working to end all genocide and persecution, and (2) recommits to combating all forms of anti-Semitism.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hres87"
    },
    "title": "Commemorating the 80th anniversary of the liberation of the Auschwitz extermination camp in Nazi-occupied Poland and International Holocaust Remembrance Day."
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution calls on the people of the United States to remember the innocent victims murdered at Auschwitz, the Jews killed during the Holocaust, and all the victims of the Nazi reign of terror.\u00a0The resolution also (1) calls on the people of the United States to continue working to end all genocide and persecution, and (2) recommits to combating all forms of anti-Semitism.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hres87"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres87ih.xml"
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
      "title": "Commemorating the 80th anniversary of the liberation of the Auschwitz extermination camp in Nazi-occupied Poland and International Holocaust Remembrance Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T09:18:38Z"
    },
    {
      "title": "Commemorating the 80th anniversary of the liberation of the Auschwitz extermination camp in Nazi-occupied Poland and International Holocaust Remembrance Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:05:39Z"
    }
  ]
}
```

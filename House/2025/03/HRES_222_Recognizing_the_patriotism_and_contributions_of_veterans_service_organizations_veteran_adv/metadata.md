# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/222
- Title: Recognizing the patriotism and contributions of veterans service organizations, veteran advocacy groups, and volunteers.
- Congress: 119
- Bill type: HRES
- Bill number: 222
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-04-28T08:06:29Z
- Update date including text: 2026-04-28T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - IntroReferral: Submitted in House
- 2025-03-14 - IntroReferral: Submitted in House
- Latest action: 2025-03-14: Submitted in House

## Actions

- 2025-03-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - IntroReferral: Submitted in House
- 2025-03-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/222",
    "number": "222",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Recognizing the patriotism and contributions of veterans service organizations, veteran advocacy groups, and volunteers.",
    "type": "HRES",
    "updateDate": "2026-04-28T08:06:29Z",
    "updateDateIncludingText": "2026-04-28T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:08:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres222ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 222\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Issa submitted the following resolution; which was referred to the Committee on Veterans' Affairs\nRESOLUTION\nRecognizing the patriotism and contributions of veterans service organizations, veteran advocacy groups, and volunteers.\nThat the House of Representatives\u2014\n**(1)**\nhonors and recognizes the patriotism and countless contributions to the United States by generations of veterans service organizations, veteran advocacy groups, and volunteers;\n**(2)**\ncommends members of veterans service organizations, veteran advocacy groups, and volunteers in the United States, territories, and abroad for their dedicated service to and support of members of the Armed Forces and veterans as well as their families and communities;\n**(3)**\nencourages the people of the United States to promote awareness of the contributions and dedication of members of veterans service organizations, veteran advocacy groups, and volunteers to members of the Armed Forces, veterans, and their families; and\n**(4)**\ncalls on the people of the United States to follow the noble example of the veterans service organizations, veteran advocacy groups, and volunteers and volunteer support and services to those who have selflessly served the United States.",
      "versionDate": "2025-03-14",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-09T15:33:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hres222",
          "measure-number": "222",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres222v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution honors and recognizes the patriotism and contributions made by generations of veterans service organizations, veteran advocacy groups, and volunteers and commends the members of such organizations for their dedicated service to members of the Armed Forces, veterans, their families, and their communities.</p><p>The resolution also encourages the people of the United States to promote awareness of the contributions and dedication of members of veterans service organizations, veteran advocacy groups, and volunteers to members of the Armed Forces, veterans, and their families. Additionally, the resolution calls on citizens to follow the example of such groups and volunteer support and services to those who have served the country.</p>"
        },
        "title": "Recognizing the patriotism and contributions of veterans service organizations, veteran advocacy groups, and volunteers."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres222.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors and recognizes the patriotism and contributions made by generations of veterans service organizations, veteran advocacy groups, and volunteers and commends the members of such organizations for their dedicated service to members of the Armed Forces, veterans, their families, and their communities.</p><p>The resolution also encourages the people of the United States to promote awareness of the contributions and dedication of members of veterans service organizations, veteran advocacy groups, and volunteers to members of the Armed Forces, veterans, and their families. Additionally, the resolution calls on citizens to follow the example of such groups and volunteer support and services to those who have served the country.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hres222"
    },
    "title": "Recognizing the patriotism and contributions of veterans service organizations, veteran advocacy groups, and volunteers."
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors and recognizes the patriotism and contributions made by generations of veterans service organizations, veteran advocacy groups, and volunteers and commends the members of such organizations for their dedicated service to members of the Armed Forces, veterans, their families, and their communities.</p><p>The resolution also encourages the people of the United States to promote awareness of the contributions and dedication of members of veterans service organizations, veteran advocacy groups, and volunteers to members of the Armed Forces, veterans, and their families. Additionally, the resolution calls on citizens to follow the example of such groups and volunteer support and services to those who have served the country.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hres222"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres222ih.xml"
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
      "title": "Recognizing the patriotism and contributions of veterans service organizations, veteran advocacy groups, and volunteers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T08:18:31Z"
    },
    {
      "title": "Recognizing the patriotism and contributions of veterans service organizations, veteran advocacy groups, and volunteers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T08:05:28Z"
    }
  ]
}
```

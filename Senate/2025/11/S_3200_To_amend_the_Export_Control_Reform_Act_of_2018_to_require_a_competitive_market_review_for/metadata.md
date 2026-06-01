# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3200
- Title: License Monopoly Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3200
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2025-12-19T20:44:02Z
- Update date including text: 2025-12-19T20:44:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3200",
    "number": "3200",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "License Monopoly Prevention Act of 2025",
    "type": "S",
    "updateDate": "2025-12-19T20:44:02Z",
    "updateDateIncludingText": "2025-12-19T20:44:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:54:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3200is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3200\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Scott of Florida (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to require a competitive market review for applications for a license to export, reexport, or in-country transfer emerging and foundational technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the License Monopoly Prevention Act of 2025 .\n#### 2. Findings; Sense of Congress\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe Bureau of Industry and Security maintains a regularly updated Entity List of foreign persons (set forth in Supplement No. 4 to part 744 of the Export Administration Regulations), including businesses, research institutions, government organizations, private organizations, individuals, and other types of legal persons, that are subject to specific license requirements for the export, reexport, or in-country transfer of specified items.\n**(2)**\nIn recent years, the number of listed foreign persons has grown significantly, and now includes private consumer companies that are not producers of traditional military or national security products.\n**(3)**\nMonopoly licenses have inadvertently been issued over the last few years, in some cases granting an exclusive right for a single company to sell a specific product to an entity on the Entity List without consideration of the market distorting impacts of these monopolies.\n**(4)**\nThe issuance of monopoly licenses creates the appearance that the Bureau of Industry and Security favors some companies at the expense of others, undermining the credibility of the bureau and undercutting the ability of the United States Government to work with the governments of allies and partners to build a shared regulatory infrastructure to control sensitive commercial technology.\n**(5)**\nMonopoly licenses have the potential to create serious distortion in the market, exacerbate economic and security vulnerabilities, and undermine fairness in the export licensing regime administered by the Bureau of Industry and Security.\n##### (b) Sense of Congress\nIt is the sense of Congress that the Department of Commerce would be well-served by a requirement that the Bureau of Industry and Security coordinate with the International Trade Administration to conduct a competitive market review when evaluating a request for a license to determine whether issuing the license would result in a single applicant having the sole license for the export, reexport, or in-country transfer of an article to similarly situated end users.\n#### 3. Requirement for competitive market review\nSection 1758(b)(3) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4817(b)(3) ) is amended by adding at the end the following:\n(D) Competitive market review (i) In general In reviewing an application for a license or other authorization for the export, reexport, or in-country transfer of technology described in paragraph (1), the Under Secretary of Commerce for Industry and Security shall conduct a competitive market review to determine whether the requested license or other authorization, if issued, would be the sole license or other authorization for the export, reexport, or in-country transfer of such technology to an end user or for an end use and may issue such license or other authorization only if the Under Secretary certifies to the appropriate congressional committees that\u2014 (I) the Under Secretary has received no other application for the export, reexport, or in-country transfer of such technology for that end user or end use; or (II) if the Under Secretary has received more than one such application, the technologies or functions of the technologies described in the applications are different to a degree that the Secretary considers the technologies to be separate technologies for purposes of issuing such license or other authorization. (ii) Consultation requirement In conducting a competitive market review required by clause (i), the Under Secretary of Commerce for Industry and Security shall consult with the Under Secretary of Commerce for International Trade. (iii) Appropriate congressional committees defined In this subparagraph, the term appropriate congressional committees means\u2014 (I) the Committee on Banking, Housing, and Urban Affairs of the Senate; and (II) the Committee on Foreign Affairs of the House of Representatives. (E) Treatment of subsequent license applications After issuing a sole license or other authorization for the export, reexport, or in-country transfer of technology described in paragraph (1), the Under Secretary of Commerce for Industry and Security shall approve any subsequent application for a license or other authorization for the same technology as the original license, unless approving such application creates a unique risk or concern that was not present at the time that the original license or other authorization was issued. .",
      "versionDate": "2025-11-19",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-12-19T20:44:02Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3200is.xml"
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
      "title": "License Monopoly Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "License Monopoly Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Export Control Reform Act of 2018 to require a competitive market review for applications for a license to export, reexport, or in-country transfer emerging and foundational technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:24Z"
    }
  ]
}
```

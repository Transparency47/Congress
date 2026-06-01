# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1456?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1456
- Title: Military Installation Retail Security Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1456
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-05-22T01:40:04Z
- Update date including text: 2025-05-22T01:40:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1456",
    "number": "1456",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Military Installation Retail Security Act of 2025",
    "type": "S",
    "updateDate": "2025-05-22T01:40:04Z",
    "updateDateIncludingText": "2025-05-22T01:40:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T18:35:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AR"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1456is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1456\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Budd (for himself, Mr. Cotton , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to establish requirements relating to long-term concessions agreements between the Secretary of Defense and retailers controlled by covered nations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military Installation Retail Security Act of 2025 .\n#### 2. Prohibition on long-term concessions agreements with retailers controlled by covered nations\nChapter 363 of title 10, United States Code, is amended by adding at the end the following new section:\n4664. Prohibition on long-term concessions agreements with retailers controlled by covered nations (a) Prohibition on future contracts The Secretary of Defense may not, on or after the date of the enactment of this section, renew, extend, or enter into a long-term concessions agreement with a retailer that is controlled by a covered nation to permit the retailer to operate or conduct business through a physical location on a covered military installation unless\u2014 (1) the Secretary waives the prohibition with respect to the retailer under subsection (c); or (2) the Committee on Foreign Investment in the United States (in this section referred to as the Committee ) determines under subsection (d) that the operation or conduct of such business by the retailer will not detrimentally affect the national security of the United States. (b) Treatment of existing contracts (1) In general Not later than 180 days after the date of the enactment of this section, the Secretary shall review each long-term concessions agreement with a covered retailer that permits the retailer to operate or conduct business through a physical location on a covered military installation\u2014 (A) to assess any direct or indirect relationships between the retailer (including any subsidiaries or parent companies of the covered retailer) and any covered nation; and (B) to determine if the retailer is controlled by a covered nation. (2) Termination If the Secretary determines under paragraph (1) that a covered retailer is controlled by a covered nation, the Secretary shall terminate the long-term concessions agreement with the retailer not later than 30 days after making that determination unless\u2014 (A) the Secretary waives the termination of the agreement under subsection (c); or (B) the Committee determines under subsection (d) that the operation or conduct by the retailer of business through a physical location on a covered military installation will not detrimentally affect the national security of the United States. (c) Waiver (1) In general The Secretary may waive the prohibition under subsection (a) with respect to a retailer or the requirement to terminate an agreement under subsection (b) with a retailer if the Secretary determines that\u2014 (A) the goods or services to be provided by the retailer are vital for the welfare and morale of members of the Armed Forces and no reasonable alternatives exist; and (B) the Secretary has implemented adequate measures to mitigate any potential national security risks posed by the retailer. (2) Report Not later than 30 days after each use of the waiver authority under paragraph (1), the Secretary shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report that includes a justification for the use of such authority and a description of any risk mitigation measures implemented under paragraph (1)(B). (d) Review by Committee on Foreign Investment in the United States of certain retailers controlled by covered nations (1) Notice required Not later than 30 days after the date of the enactment of this section, a covered retailer shall submit to the Committee a notice that includes a description of any direct or indirect relationships between the retailer (including any subsidiaries or parent companies of the retailer) and any covered nation. (2) Investigation The Committee shall conduct an investigation of the effects on the national security of the United States of each covered retailer operating or conducting business through a physical location on a covered military installation, including an assessment of any direct or indirect relationships between the retailer (including any subsidiaries or parent companies of the retailer) and any covered nation. (3) Determination Not later than 180 days after completing an investigation under paragraph (2) with respect to a covered retailer, the Committee shall submit to the Secretary a determination with respect to whether the retailer operating or conducting business through a physical location on a covered military installation will detrimentally affect the national security of the United States. (4) Annual reports A covered retailer that receives a determination under paragraph (3) that the operation or conduct by the retailer of business through a physical location on a covered military installation will not detrimentally affect the national security of the United States shall submit to the Committee, not less frequently than annually, disclosures regarding any change in the ownership structure of the retailer that may affect whether or not the covered retailer is controlled by a covered nation. (e) Termination The Secretary shall terminate a long-term concession agreement with a covered retailer if the Secretary determines that the retailer\u2014 (1) has failed to comply with the requirements of subsection (d); or (2) has misrepresented the ownership or control of the retailer in order to evade the prohibition under subsection (a) or the requirement to terminate an agreement under subsection (b). (f) Definitions In this section: (1) The term controlled by a covered nation means, with respect to a retailer, that\u2014 (A) the retailer is organized under the laws of a covered nation or any jurisdiction within a covered nation; (B) a covered nation owns 20 percent or more of the equity interest in the retailer; or (C) the retailer is subject to the direction or control of a covered nation. (2) The term covered military installation means a military installation (as defined in section 2801 of this title) located in the United States. (3) The term covered nation has the meaning given that term in section 4872 of this title. (4) The term covered retailer means a retailer that is performing a long-term concessions agreement on or before the date of the enactment of this section. (5) The term long-term concessions agreement means a contract, subcontract (at any tier), or other agreement, including a lease agreement or licensing agreement, to operate a business through a physical location on a covered military installation entered into by\u2014 (A) the Secretary of Defense or a Secretary of a military department and a person, including a nonappropriated fund instrumentality; or (B) a person and a nonappropriated fund instrumentality. (6) The term nonappropriated fund instrumentality has the meaning given that term in section 2488 of this title. (7) The term retailer means\u2014 (A) a nonappropriated fund instrumentality that operates or seeks to operate a business through a physical location on a covered military installation; or (B) any other person that operates or seeks to operate a business on a covered military installation under a contract, subcontract (at any tier), or other agreement, including a lease agreement or licensing agreement, with\u2014 (i) a nonappropriated fund instrumentality; (ii) the Secretary of Defense; or (iii) a Secretary of a military department. .",
      "versionDate": "2025-04-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-22T01:40:03Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1456is.xml"
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
      "title": "Military Installation Retail Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Military Installation Retail Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to establish requirements relating to long-term concessions agreements between the Secretary of Defense and retailers controlled by covered nations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:36Z"
    }
  ]
}
```

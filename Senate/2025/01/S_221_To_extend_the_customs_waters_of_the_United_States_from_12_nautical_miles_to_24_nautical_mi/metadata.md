# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/221?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/221
- Title: Extending Limits of United States Customs Waters Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 221
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-05-02T20:35:05Z
- Update date including text: 2025-05-02T20:35:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/221",
    "number": "221",
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
    "title": "Extending Limits of United States Customs Waters Act of 2025",
    "type": "S",
    "updateDate": "2025-05-02T20:35:05Z",
    "updateDateIncludingText": "2025-05-02T20:35:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T19:28:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NH"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s221is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 221\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Scott of Florida (for himself, Ms. Hassan , Mr. Lankford , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo extend the customs waters of the United States from 12 nautical miles to 24 nautical miles from the baselines of the United States, consistent with Presidential Proclamation 7219.\n#### 1. Short title\nThis Act may be cited as the Extending Limits of United States Customs Waters Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nOn December 27, 1988, Presidential Proclamation 5928 extended the territorial sea of the United States from 3 nautical miles to 12 nautical miles from the baselines of the United States, determined in accordance with international law.\n**(2)**\nOn August 2, 1999, Presidential Proclamation 7219 extended the contiguous zone of the United States from 12 nautical miles to 24 nautical miles from the baselines of the United States, determined in accordance with international law, but in no case within the territorial sea of another country.\n**(3)**\nCustomary international law, in its current form, as provided for in the United Nations Convention on the Law of the Sea and consistent with Presidential Proclamations 5928 and 7219, reflects that\u2014\n**(A)**\nevery coastal State has the right to establish the breadth of its territorial sea to a limit not exceeding 12 nautical miles, measured from its baselines;\n**(B)**\na coastal State\u2019s contiguous zone may not extend beyond 24 nautical miles from the baselines from which the breadth of the territorial sea is measured;\n**(C)**\na coastal State has exclusive jurisdiction over its flagged vessels within its territorial seas and upon the high seas; and\n**(D)**\nin the contiguous zone of a coastal State, the State may\u2014\n**(i)**\nexercise the control necessary to prevent the infringement of its customs, fiscal, immigration, or sanitary laws and regulations within its territory or the territorial sea; and\n**(ii)**\npunish the infringement of those laws and regulations committed within its territory or the territorial sea.\n**(4)**\nCustomary international law, in its current form, as provided for in the United Nations Convention on the Law of the Sea, recognizes that outside the territorial waters of a coastal State, the vessels and aircraft of all countries enjoy the high seas freedoms of navigation and overflight. Pursuant to those freedoms and the requirements of international law\u2014\n**(A)**\nbefore boarding a vessel outside of the territorial waters of a coastal State, but within the contiguous zone of that State, authorities of the State are generally required to have reasonable grounds to believe that the vessel is destined for the State or has violated or is attempting to violate the customs, fiscal, immigration, or sanitary laws and regulations of that State; and\n**(B)**\nthe hot pursuit of a foreign vessel\u2014\n**(i)**\nmay be undertaken when competent authorities of the State have good reason to believe that the vessel or one of its boats has violated the laws and regulations of that State;\n**(ii)**\nis required to be commenced when the foreign vessels or one of its boats is within the internal waters, the territorial sea, or the contiguous zone of the State, and may be continued outside the territorial sea or the contiguous zone only if the pursuit has not been interrupted; and\n**(iii)**\nin a case in which the foreign vessels is within the contiguous zone of the State, may be undertaken only if there has been a violation of the rights for the protection of which the contiguous zone was established.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nit is necessary to extend the authority of U.S. Customs and Border Protection to conduct law enforcement activities in the customs waters of the United States from 12 nautical miles to 24 nautical miles because as modern technology continues to change and expand rapidly, the performance and speed of maritime vessels, including those used to violate the laws of the United States or evade United States law enforcement agents, improve, and the limit of 12 nautical miles no longer provides law enforcement agents with sufficient time to interdict such vessels; and\n**(2)**\nthe extension of the customs waters of the United States to the limits permitted by international law will advance the law enforcement and public health interests of the United States.\n#### 3. Extension of customs waters of the United States\n##### (a) Tariff Act of 1930\nSection 401(j) of the Tariff Act of 1930 ( 19 U.S.C. 1401(j) ) is amended\u2014\n**(1)**\nby striking means, in the case and inserting the following:\nmeans\u2014 (1) in the case ;\n**(2)**\nby striking of the coast of the United States and inserting from the baselines of the United States (determined in accordance with international law) ;\n**(3)**\nby striking and, in the case and inserting the following:\n; and (2) in the case ; and\n**(4)**\nby striking the waters within four leagues of the coast of the United States. and inserting the following:\nthe waters within\u2014 (A) the territorial sea of the United States, to the limits permitted by international law in accordance with Presidential Proclamation 5928 of December 27, 1988; and (B) the contiguous zone of the United States, to the limits permitted by international law in accordance with Presidential Proclamation 7219 of September 2, 1999. .\n##### (b) Anti-Smuggling Act\nSection 401(c) of the Anti-Smuggling Act ( 19 U.S.C. 1709(c) ) is amended\u2014\n**(1)**\nby striking means, in the case and inserting the following:\nmeans\u2014 (1) in the case ;\n**(2)**\nby striking of the coast of the United States and inserting from the baselines of the United States (determined in accordance with international law) ;\n**(3)**\nby striking and, in the case and inserting the following:\n; and (2) in the case ; and\n**(4)**\nby striking the waters within four leagues of the coast of the United States. and inserting the following:\nthe waters within\u2014 (A) the territorial sea of the United States, to the limits permitted by international law in accordance with Presidential Proclamation 5928 of December 27, 1988; and (B) the contiguous zone of the United States, to the limits permitted by international law in accordance with Presidential Proclamation 7219 of September 2, 1999. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the day after the date of the enactment of this Act.",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1268",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Extending Limits of U.S. Customs Waters Act",
      "type": "HR"
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
        "updateDate": "2025-05-01T17:49:04Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s221is.xml"
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
      "title": "Extending Limits of United States Customs Waters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T13:18:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Extending Limits of United States Customs Waters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:36Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend the customs waters of the United States from 12 nautical miles to 24 nautical miles from the baselines of the United States, consistent with Presidential Proclamation 7219.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:16Z"
    }
  ]
}
```

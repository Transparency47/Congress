# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1103?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1103
- Title: Vessel Tracking for Sanctions Enforcement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1103
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-05-12T18:14:35Z
- Update date including text: 2025-05-12T18:14:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1103",
    "number": "1103",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Vessel Tracking for Sanctions Enforcement Act of 2025",
    "type": "S",
    "updateDate": "2025-05-12T18:14:35Z",
    "updateDateIncludingText": "2025-05-12T18:14:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T15:22:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "OK"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "MS"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1103is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1103\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Ms. Hassan (for herself, Mr. Lankford , Mr. Wicker , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require a pilot program on the use of big data analytics to identify vessels evading sanctions and export controls and to require a report on the availability in the United States of emerging and foundational technologies subject to export controls.\n#### 1. Short title\nThis Act may be cited as the Vessel Tracking for Sanctions Enforcement Act of 2025 .\n#### 2. Pilot program on use of big data analytics to identify vessels evading sanctions and export controls\n##### (a) In general\nNot later than 18 months after the date of the enactment of this Act, the Secretary of Homeland Security, acting through the Commissioner of U.S. Customs and Border Protection, shall establish a pilot program at the National Targeting Center to assess the feasibility and advisability of using big data analytics to identify and predict instances in which disabling or manipulating the Automatic Identification System on a vessel is an indication that there is a high risk that the vessel is transporting goods in a manner that evades sanctions or export controls imposed by the United States.\n##### (b) Law enforcement use\nThe Secretary, acting through the Commissioner, shall design the pilot program required by subsection (a) to provide actionable intelligence with respect to instances described in subsection (a) to\u2014\n**(1)**\noperational components of the Department of Homeland Security, including U.S. Immigration and Customs Enforcement and the Coast Guard;\n**(2)**\nother Federal law enforcement agencies; and\n**(3)**\nsuch agencies of foreign countries that are partners of the United States as the Secretary considers appropriate.\n##### (c) Data elements\n**(1) In general**\nIn developing the pilot program required by subsection (a), the Secretary, acting through the Commissioner, shall consider the inclusion of the following data with respect to a vessel described in that subsection:\n**(A)**\nThe type of goods being transported on the vessel.\n**(B)**\nThe destination of the vessel.\n**(C)**\nThe ownership and nationality of the vessel, the shipper, and the importer.\n**(D)**\nThe ownership and nationality of vessels located in close proximity to the vessel while the Automatic Identification System was disabled or being manipulated.\n**(E)**\nThe period of time for which the Automatic Identification System on the vessel was disabled or being manipulated.\n**(F)**\nThe frequency of issues with the Automatic Identification System on that vessel.\n**(2) Data models**\nThe pilot program required by subsection (a) may include multiple data models to account for different behavior patterns for different shippers and different types of goods.\n##### (d) Interagency coordination\nThe Secretary, acting through the Commissioner, shall coordinate with the Secretary of Commerce and the Director of National Intelligence in developing and carrying out the pilot program required by subsection (a).\n##### (e) Termination\nThe pilot program required by subsection (a) shall terminate on the date that is 4 years after the date of the enactment of this Act.\n##### (f) Report required\nNot later than 4 years after the date of the enactment of this Act, the Secretary of Homeland Security, in consultation with the Secretary of Commerce , the Secretary of the Treasury, and the Director of National Intelligence, shall submit to Congress a report\u2014\n**(1)**\nassessing the usefulness of the pilot program required by subsection (a) in identifying and predicting instances described in that subsection;\n**(2)**\nwith respect to each instance in which a vessel was identified under the pilot program as posing a high risk of transporting goods in a manner that evades sanctions or export controls imposed by the United States and the vessel was successfully interdicted by the United States or a country that is a partner of the United States\u2014\n**(A)**\nspecifying whether or not the vessel was confirmed to be evading such sanctions or export controls;\n**(B)**\nif the vessel was confirmed to be evading such sanctions or export controls, specifying the penalty imposed; and\n**(C)**\nif the vessel was not confirmed to be evading such sanctions or export controls, specifying whether a United States agency took action against the vessel based on reasonable suspicion;\n**(3)**\nwith respect to each instance in which a vessel was identified under the pilot program as posing a high risk of transporting goods in a manner that evades sanctions or export controls imposed by the United States and the vessel was not successfully interdicted by the United States or a country that is a partner of the United States, specifying whether the vessel traveled to\u2014\n**(A)**\na country with respect to which the United States has imposed sanctions or export controls with respect to goods suspected of being transported on the vessel;\n**(B)**\na country not described in subparagraph (A) but that the Secretary of Homeland Security has identified as a country posing a high risk of transshipment of goods suspected of being transported on the vessel to a country described in subparagraph (A); or\n**(C)**\na country not described in subparagraph (A) or (B); and\n**(4)**\nmaking recommendations with respect to whether big data analytics should be used to identify and predict instances described in subsection (a) in the future.\n##### (g) No additional amounts authorized\nNo additional amounts are authorized to be appropriated to carry out the pilot program required by subsection (a).\n##### (h) Rule of construction on collection or acquisition of information\nNothing in this section authorizes any new collection or acquisition of information not otherwise authorized by existing law as of the date of the enactment of this Act.",
      "versionDate": "2025-03-25",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-12T18:14:35Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1103is.xml"
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
      "title": "Vessel Tracking for Sanctions Enforcement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Vessel Tracking for Sanctions Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a pilot program on the use of big data analytics to identify vessels evading sanctions and export controls and to require a report on the availability in the United States of emerging and foundational technologies subject to export controls.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:48:28Z"
    }
  ]
}
```

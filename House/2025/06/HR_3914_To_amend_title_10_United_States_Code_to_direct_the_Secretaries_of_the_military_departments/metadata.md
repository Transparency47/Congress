# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3914?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3914
- Title: Valor Has No Expiration Act
- Congress: 119
- Bill type: HR
- Bill number: 3914
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-12-12T09:08:17Z
- Update date including text: 2025-12-12T09:08:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3914",
    "number": "3914",
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
    "title": "Valor Has No Expiration Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:08:17Z",
    "updateDateIncludingText": "2025-12-12T09:08:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3914ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3914\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Issa introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to direct the Secretaries of the military departments to review certain requests to award decorations that were not timely awarded because relevant records were classified or otherwise restricted, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Valor Has No Expiration Act .\n#### 2. Review of requests for decorations not timely awarded to members of certain Armed Forces serving on active duty because relevant records were classified or otherwise restricted\nChapter 57 of title 10, United States Code, is amended by inserting after section 1130 the following new section:\n1130a. Consideration of proposals for certain decorations not previously submitted in timely fashion because relevant records were classified or otherwise restricted (a) Waiver of time limitations Notwithstanding section 1130 of this title, a decoration (including any device in lieu of a decoration), authorized by law or under the regulations of the Department of Defense or the military department concerned, may be awarded, without regard to any time limitation imposed by law or regulation for a recommendation for such award\u2014 (1) to any person for service\u2014 (A) while on active duty in the Army, Navy, Marine Corps, Air Force, or Space Force; (B) during the period beginning on January 1, 1940; and (C) the records of which were classified, withheld from the public record due to sensitivity, or redacted for national security purposes; and (2) based on a request for consideration of such award received by the Secretary of a military department. (b) Review of requests In carrying out this section, the Secretary of a military department\u2014 (1) shall\u2014 (A) begin a review of a request under subsection (a)(2) not later than 30 days after the Secretary receives such request; and (B) complete such a review not later than one year after the date of such receipt; and (2) may use the process under subsections (b) and (c) of section 1130 of this title to carry out such a review. (c) Rules of construction (1) The failure of the Secretary of a military department to complete the review of a request under subsection (a)(2) within the time limitations under subsection (b) shall not be construed to limit the authority to award a decoration under this section. (2) In the case of a decoration the President may award, the recommendation of the Secretary of the military department concerned to not award such decoration shall not be construed to prohibit the President from awarding such decoration. (d) Reports (1) (A) Not later than 30 days after completing the review of a request under subsection (b), the Secretary of a military department shall submit to the Committees on Armed Services of the Senate and House of Representatives a report regarding such review. (B) In the case of a review of a request for a decoration the President may award, the Secretary of the military department concerned shall, subject to subparagraph (C), also submit such report to the President. (C) In the case of a review of a request for a Medal of Honor, the Secretary of Defense shall submit the report under this paragraph. (2) Such a report shall include, with respect to the request reviewed, the following elements: (A) A summary of the request. (B) The findings of the review. (C) The final action or recommendation of the submitting Secretary regarding such request. (D) Any recommendation of the submitting Secretary to improve award procedures with respect to military intelligence personnel. .",
      "versionDate": "2025-06-11",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-16T15:23:06Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3914ih.xml"
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
      "title": "Valor Has No Expiration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Valor Has No Expiration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to direct the Secretaries of the military departments to review certain requests to award decorations that were not timely awarded because relevant records were classified or otherwise restricted, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T06:18:26Z"
    }
  ]
}
```

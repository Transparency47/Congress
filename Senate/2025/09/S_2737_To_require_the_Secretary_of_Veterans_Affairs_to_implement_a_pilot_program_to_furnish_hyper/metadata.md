# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2737?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2737
- Title: Veterans National Traumatic Brain Injury Treatment Act
- Congress: 119
- Bill type: S
- Bill number: 2737
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2026-01-09T16:39:11Z
- Update date including text: 2026-01-09T16:39:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2737",
    "number": "2737",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Veterans National Traumatic Brain Injury Treatment Act",
    "type": "S",
    "updateDate": "2026-01-09T16:39:11Z",
    "updateDateIncludingText": "2026-01-09T16:39:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
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
        "item": [
          {
            "date": "2025-12-10T21:00:32Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-09T16:04:31Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2737is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2737\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Mr. Tuberville introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to implement a pilot program to furnish hyperbaric oxygen therapy to certain veterans through community care providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans National Traumatic Brain Injury Treatment Act .\n#### 2. Pilot program to furnish hyperbaric oxygen therapy to a veteran with traumatic brain injury or post-traumatic stress disorder\n##### (a) Establishment\nThe Secretary of Veterans Affairs shall implement a pilot program to furnish HBOT to a veteran who has a traumatic brain injury or post-traumatic stress disorder through a health care provider described in section 1703(c)(5) of title 38, United States Code (in this section referred to as the pilot program ).\n##### (b) Locations\nThe Secretary shall select two Veterans Integrated Service Networks of the Department of Veterans Affairs in which to operate the pilot program.\n##### (c) Accreditation required\nThe Secretary shall ensure that any medical facility at which a veteran receives HBOT under the pilot program is accredited by\u2014\n**(1)**\nthe Joint Commission on Accreditation of Hospital Organizations;\n**(2)**\nthe Undersea and Hyperbaric Medical Society; or\n**(3)**\nanother appropriate organization that has expertise and objectivity comparable to that of the Joint Commission on Accreditation of Hospital Organizations or the Undersea and Hyperbaric Medical Society.\n##### (d) Funding\n**(1) In general**\nThere is in the general fund of the Treasury a fund to be known as the VA HBOT Fund (in this section referred to as the Fund ).\n**(2) Sole source of funds**\nThe sole source of amounts deposited into the Fund shall be donations received by the Secretary for the express purpose of providing HBOT under the pilot program.\n**(3) Availability**\nAmounts in the Fund shall be available to the Secretary without fiscal year limitation to pay for HBOT under the pilot program.\n##### (e) Termination\nThe pilot program and the Fund shall terminate on the day that is three years after the date of the enactment of this Act.\n##### (f) HBOT defined\nIn this section, the term HBOT means hyperbaric oxygen therapy provided to a patient with a medical device\u2014\n**(1)**\napproved by the Food and Drug Administration; or\n**(2)**\nissued an investigational device exemption by the Food and Drug Administration.\n#### 3. Comptroller General report on use of hyperbaric oxygen therapy to treat traumatic brain injury and post-traumatic stress disorder\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives an update to the report of the Comptroller General published on December 18, 2015, and titled Research on Hyperbaric Oxygen Therapy to Treat Traumatic Brain Injury and Post-Traumatic Stress Disorder (GAO\u201316\u2013154).\n##### (b) Elements\nThe update required under subsection (a) shall include an assessment by the Comptroller General of clinical trials conducted since the publication of the report specified in such subsection\u2014\n**(1)**\nregarding the use of hyperbaric oxygen therapy to treat traumatic brain injury and post-traumatic stress disorder; and\n**(2)**\nby\u2014\n**(A)**\nthe Secretary of Veterans Affairs;\n**(B)**\nthe Secretary of Defense; and\n**(C)**\nprivate entities.\n#### 4. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking November 30, 2031 and inserting October 30, 2034 .",
      "versionDate": "2025-09-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-09T16:38:57Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2026-01-09T16:38:47Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-01-09T16:38:51Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-09T16:39:01Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-01-09T16:39:11Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2026-01-09T16:38:42Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-01-09T16:39:06Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2026-01-09T16:38:36Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-01-09T16:35:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-23T15:32:57Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2737is.xml"
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
      "title": "Veterans National Traumatic Brain Injury Treatment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans National Traumatic Brain Injury Treatment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Veterans Affairs to implement a pilot program to furnish hyperbaric oxygen therapy to certain veterans through community care providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:16Z"
    }
  ]
}
```

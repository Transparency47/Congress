# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7784?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7784
- Title: Secure Tracks Act
- Congress: 119
- Bill type: HR
- Bill number: 7784
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-04-29T08:06:55Z
- Update date including text: 2026-04-29T08:06:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7784",
    "number": "7784",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Secure Tracks Act",
    "type": "HR",
    "updateDate": "2026-04-29T08:06:55Z",
    "updateDateIncludingText": "2026-04-29T08:06:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7784ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7784\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Ms. Titus introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to establish requirements regarding visual and automated track inspections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Tracks Act .\n#### 2. Track inspections\n##### (a) In general\nSubchapter II of chapter 201 of title 49, United States Code, is amended by adding at the end the following:\n20172. Visual and automated track inspection requirements (a) Minimum frequency for visual track inspections All main line track designated for operation at Class 3 track speeds or higher under section 213.9 of title 49, Code of Federal Regulations, as in effect on January 1, 2026, shall be subject to visual inspection by a qualified inspector not less frequently than twice each week, with at least 1 calendar day between each inspection. (b) Immediate remediation of safety defects Any defect or unsafe condition identified by any inspection, detection, or monitoring method shall be corrected, protected, or removed from service immediately upon detection, consistent with the requirements of part 213 of title 49, Code of Federal Regulations, as in effect on January 1, 2026. (c) Remediation by qualified person If a qualified inspector making a track inspection under this section finds a deviation from the requirements of part 213 of title 49, Code of Federal Regulations, as in effect on January 1, 2026, the qualified inspector shall\u2014 (1) immediately initiate remedial action; and (2) have the sole authority to authorize any subsequent movements to facilitate repairs on track that is out of service. (d) Prohibition on granting waivers that reduce safety coverage Notwithstanding any other provision of law, including section 20103 of this title, the Secretary of Transportation may not grant a waiver, exemption, or modification of any safety regulation issued under chapter II of subtitle B of title 49, Code of Federal Regulations, as in effect on January 1, 2026, if the proposed alternative inspection, detection, or monitoring method fails to identify or detect all defect conditions defined or recognized as unsafe under applicable Federal Railroad Administration regulations. (e) Automated track inspection requirements Not later than 1 year after the date of the enactment of this section, the Secretary shall update subparts F and G of part 213 of title 49, Code of Federal Regulations, to require that a Track Geometry Measurement System operate over the following track classifications at the following frequencies and be subject to the following requirements regarding TGMS inspections: (1) For operations at a qualified cant deficiency (Eu) of more than 5 inches on Classes 1 through 5 track, at least 4 times per calendar year, with at least 43 days elapsing between TGMS inspections. (2) For Class 1 track operating more than 15,000,000 gross tons annually, at least once per calendar year, with at least 170 days elapsing between TGMS inspections. (3) For Class 2 track\u2014 (A) operating 15,000,000 or fewer gross tons annually, at least once per calendar year, with at least 170 days elapsing between TGMS inspections; and (B) operating more than 15,000,000 gross tons annually, at least twice per calendar year, with at least 120 days elapsing between TGMS inspections. (4) For Class 3 track\u2014 (A) operating 15,000,000 or fewer gross tons annually, at least twice per calendar year, with at least 120 days elapsing between TGMS inspections; and (B) operating more than 15,000,000 gross tons annually, at least 3 times per calendar year, with at least 90 days elapsing between TGMS inspections. (5) For Class 4 track\u2014 (A) operating 15,000,000 or fewer gross tons annually, at least 3 times per calendar year, with at least 90 days elapsing between TGMS inspections; and (B) operating more than 15,000,000 gross tons annually, at least 4 times per calendar year, with at least 43 days elapsing between TGMS inspections. (6) For Class 5 track, at least 4 times per calendar year, with at least 43 days elapsing between TGMS inspections. (7) For Class 6 and Class 7 track, at least twice during any 120-day period, with at least 25 days elapsing between TGMS inspections. (8) For Class 8 track, at least twice during any 60-day period, with at least 12 days elapsing between TGMS inspections. (9) For Class 9 track, at least twice during any 30-day period, with at least 6 days elapsing between TGMS inspections. (10) For crossovers where the track speed is more than 30 miles per hour, at least twice per calendar year, with at least 120 days elapsing between TGMS inspections. (f) Fixing deviation requirements Not later than 1 year after the date of the enactment of this section, the Secretary shall update part 213 of title 49, Code of Federal Regulations, as in effect on January 1, 2026, to require that when any inspection, whether done by a qualified inspector or by a machine (including a TGMS machine), finds a deviation from the requirements of this part, the qualified inspector or other authorized personnel shall immediately remediate the deviation in accordance with such part. (g) Applicable requirements The Secretary shall ensure that any requirements of subparts F and G of part 213 of title 49, Code of Federal Regulations, as in effect on January 1, 2026, including section 213.333 of such part, generated by an update to the regulations made pursuant to subsection (e) or (f) are applied to the applicable track classification. (h) Definitions In this section: (1) Class 1 track; Class 2 track; Class 3 track; Class 4 track; Class 5 track The terms Class 1 track , Class 2 track , Class 3 track , Class 4 track , and Class 5 track means Class 1 track, Class 2 track, Class 3 track, Class 4 track, and Class 5 track, respectively, as such terms are used in section 213.9(a) of title 49, Code of Federal Regulations, as in effect on January 1, 2026. (2) Main line The term main line has the meaning given such term in section 236.1003 of title 49, Code of Federal Regulations, as in effect on January 1, 2026. (3) Qualified inspector The term qualified inspector means a person designated as a qualified person to inspect track for defects under section 213.7(b) of title 49, Code of Federal Regulations, as in effect on January 1, 2026. (4) Track Geometry Measurement System; TGMS The terms Track Geometry Measurement System and TGMS means a Track Geometry Measurement System as such term is used in section 213.333 of title 49, Code of Federal Regulations, as in effect on January 1, 2026. .\n##### (b) Clerical amendment\nThe analysis for chapter 201 of title 49, United States Code, is amended by adding at the end the following:\n20172. Visual and automated track inspection requirements. .",
      "versionDate": "2026-03-04",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-27T20:19:23Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7784ih.xml"
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
      "title": "Secure Tracks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure Tracks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to establish requirements regarding visual and automated track inspections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:20Z"
    }
  ]
}
```

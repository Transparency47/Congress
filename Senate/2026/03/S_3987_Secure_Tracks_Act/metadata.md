# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3987
- Title: Secure Tracks Act
- Congress: 119
- Bill type: S
- Bill number: 3987
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-03-23T20:37:28Z
- Update date including text: 2026-03-23T20:37:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3987",
    "number": "3987",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Secure Tracks Act",
    "type": "S",
    "updateDate": "2026-03-23T20:37:28Z",
    "updateDateIncludingText": "2026-03-23T20:37:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T18:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3987is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3987\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Ms. Baldwin (for herself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49 to include certain requirements regarding visual track inspections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Tracks Act .\n#### 2. Track inspections\n##### (a) In general\nSubchapter II of chapter 201 of title 49, United States Code, is amended by adding at the end the following:\n20172. Protecting visual track inspections and incorporating automated track inspections (a) Definitions In this section: (1) Class 1 track; Class 2 track; Class 3 track; Class 4 track; Class 5 track The terms Class 1 track , Class 2 track , Class 3 track , Class 4 track , and Class 5 track have the meanings given such terms in section 213.9(a) of title 49, Code of Federal Regulations (as in effect on January 1, 2026). (2) Main line The term Main line has the meaning given such term in section 236.1003 of title 49, Code of Federal Regulations (as in effect on January 1, 2026). (3) Qualified inspector The term qualified inspector means a person designated as a qualified person to inspect track for defects under section 213.7(b) of title 49, Code of Federal Regulations (as in effect on January 1, 2026). (4) Track Geometry Measurement System The term Track Geometry Measurement System has the meaning given such term in section 213.333 of title 49, Code of Federal Regulations (as in effect on January 1, 2026). (b) Minimum frequency for visual track inspections All main line track designated for operation at Class 3 speeds or higher under section 213.9 of title 49, Code of Federal Regulations, shall be subject to visual inspection not less frequently than twice each week, with at least 1 calendar day interval between each inspections by a qualified inspector. (c) Immediate remediation of safety defects Any defect or unsafe condition identified by any inspection, detection, or monitoring method shall be corrected, protected, or removed from service immediately upon detection, consistent with the requirements of part 213 of title 49, Code of Federal Regulations. (d) Remediation by qualified person If a qualified inspector making track inspections finds a deviation from the requirements of part 213 of title 49, Code of Federal Regulations, the qualified inspector shall\u2014 (1) immediately initiate remedial action; and (2) have the sole authority to authorize any subsequent movements to facilitate repairs on track that is out of service. (e) Prohibition on granting waivers that reduce safety coverage Notwithstanding any other provision of law, including section 20103 of this title, the Secretary of Transportation may not grant a waiver, exemption, or modification of any safety regulation issued under chapter II of subtitle B of title 49, Code of Federal Regulations, if the proposed alternative inspection, detection, or monitoring method fails to identify or detect all defect conditions defined or recognized as unsafe under applicable Federal Railroad Administration regulations. (f) Automated track inspection requirements Not later than 1 year after the date of the enactment of this section, the Secretary shall update subparts F and G of part 213 of title 49, Code of Federal Regulations, to require that a qualifying Track Geometry Measurement System (in this section referred to as TGMS ) operate over the following track classifications at the following frequencies: (1) For operations at a qualified cant deficiency (E u ) of more than 5 inches on Classes 1 through 5 track, TGMS shall operate at least 4 times per calendar year and at least 43 days shall elapse between TGMS inspections. (2) For Class 1 track, operating more than 15,000,000 gross tons annually, TGMS shall operate at least once per calendar year and at least 170 days shall elapse between TGMS inspections. (3) For Class 2 track\u2014 (A) operating less than 15,000,000 gross tons annually, TGMS shall operate at least once per calendar year and at least 170 days shall elapse between TGMS inspections; and (B) operating more than 15,000,000 gross tons annually, TGMS shall operate at least twice per calendar year and at least 120 days shall elapse between TGMS inspections. (4) For Class 3 track\u2014 (A) operating fewer than 15,000,000 gross tons annually, TGMS shall operate at least twice per calendar year and at least 120 days shall elapse between TGMS inspections; and (B) operating more than 15,000,000 gross tons annually, TGMS shall operate at least 3 times per calendar year and at least 90 days shall elapse between TGMS inspections. (5) For Class 4 track\u2014 (A) operating fewer than 15,000,000 gross tons annually, TGMS shall operate at least 3 times per calendar year and at least 90 days shall elapse between TGMS inspections; and (B) operating more than 15,000,000 gross tons annually, TGMS shall operate at least 4 times per calendar year and at least 43 days shall elapse between TGMS inspections. (6) For Class 5 track, TGMS shall operate at least 4 times per calendar year and at least 43 days shall elapse between TGMS inspections. (7) For Class 6 and Class 7 track, TGMS shall operate at least twice within any 120-day period and at least 25 days shall elapse between TGMS inspections. (8) For Class 8 track, TGMS shall operate at least twice within any 60-day period and at least 12 days shall elapse between TGMS inspections. (9) For Class 9 track, TGMS shall operate at least twice within any 30-day period and at least 6 days shall elapse between TGMS inspections. (10) For crossovers where the track speed is more than 30 miles per hour, TGMS shall operate at least twice per calendar year and at least 120 days shall elapse between TGMS inspections. (g) Fixing deviation requirements Not later than 1 year after the date of the enactment of this section, the Secretary shall update part 213 of title 49, Code of Federal Regulations, to require that when any inspection, whether done by a qualified inspector or by a machine (including a TGMS machine), finds a deviation from the requirements of this part, the qualified inspector or other authorized personnel shall immediately remediate the deviation in accordance with part 213 of title 49, Code of Federal Regulations. (h) Applicable requirements The Secretary shall ensure that any requirements under subparts F and G of part 213 of title 49, Code of Federal Regulations, including section 213.333, generated by an update to the regulations made pursuant to subsection (f) or subsection (g) are applied to the applicable track Class. .\n##### (b) Clerical amendment\nThe analysis for chapter 201 of title 49, United States Code, is amended by adding at the end the following:\n20172. Protecting visual track inspections and incorporating automated track inspection. .",
      "versionDate": "",
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
        "updateDate": "2026-03-23T20:37:28Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3987is.xml"
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
      "title": "Secure Tracks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure Tracks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49 to include certain requirements regarding visual track inspections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:33:43Z"
    }
  ]
}
```

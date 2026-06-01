# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4539?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4539
- Title: Protecting Charitable Giving Act
- Congress: 119
- Bill type: S
- Bill number: 4539
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-28T20:38:06Z
- Update date including text: 2026-05-28T20:38:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4539",
    "number": "4539",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Protecting Charitable Giving Act",
    "type": "S",
    "updateDate": "2026-05-28T20:38:06Z",
    "updateDateIncludingText": "2026-05-28T20:38:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T17:13:47Z",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4539is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4539\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mr. Young (for himself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the penalties relating to the disclosure of tax return information relating to contributors to certain tax-exempt organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Charitable Giving Act .\n#### 2. Unauthorized disclosure of information relating to contributors to certain tax-exempt organizations\n##### (a) In general\nSection 7213 of the Internal Revenue Code of 1986 is amended by redesignating subsection (e) as subsection (f) and by inserting after subsection (d) the following new subsection:\n(e) Special rules for disclosures of contributors to certain tax-Exempt organizations (1) Increased penalty In the case of any disclosure of form 990 schedule B return information, paragraphs (1), (2), (3), and (4) of subsection (a) shall each be applied by substituting not less than $10,000 and not exceeding $250,000 for not exceeding $5,000 . (2) Venue (A) In general A prosecution for an offense under paragraphs (1), (2), (3), or (4) of subsection (a) relating to the disclosure of form 990 schedule B return information may be brought in\u2014 (i) the judicial district in which a victim of the offense resides, or (ii) any other judicial district with jurisdiction otherwise provided for by law. (B) Residency For purposes of determining venue under this paragraph\u2014 (i) an individual shall be deemed to reside in the judicial district in which that individual is domiciled, and (ii) an organization shall be deemed to reside in the judicial district in which the organization maintains its principal place of business. (C) Victim For purposes of this paragraph, the term victim includes\u2014 (i) the organization whose form 990 schedule B information was disclosed, and (ii) any contributor to such organization who is described in paragraph (3)(B). (3) Form 990 schedule B information For purposes of this subsection, the term form 990 schedule B information means any information which\u2014 (A) is return information (as defined in section 6103(b)) of\u2014 (i) an organization described in section 501(c)(3) (other than a private foundation, as defined in section 509(a)), or (ii) an organization described in section 501(c)(4), and (B) contains the names or address of any contributor to such organization. .\n##### (b) Effective date\nThe amendments made by this section shall apply to disclosures made after the date of the enactment of this Act.\n#### 3. Audits and reports on unauthorized disclosures relating to contributors of certain tax-exempt organizations\nSection 7803(d)(3) of the Internal Revenue Code of 1986 is amended by striking and at the end of subparagraph (B), by striking the period at the end of subparagraph (C) and inserting ; and , and by adding at the end the following new subparagraph:\n(D) issue a report with respect to any disclosure of form 990 schedule B information (as defined in section 7213(e)(3)) to which section 7213(e) applies, which report shall\u2014 (i) describe the result of an audit on the occurrence of such disclosure, (ii) recommend steps to prevent similar further such disclosures in the future, and (iii) be appropriately redacted to protect any return information (as defined in section 6103(b)). .",
      "versionDate": "2026-05-14",
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
        "name": "Taxation",
        "updateDate": "2026-05-28T20:38:05Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4539is.xml"
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
      "title": "Protecting Charitable Giving Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T02:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Charitable Giving Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify the penalties relating to the disclosure of tax return information relating to contributors to certain tax-exempt organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T02:18:27Z"
    }
  ]
}
```

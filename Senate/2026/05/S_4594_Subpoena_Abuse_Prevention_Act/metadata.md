# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4594?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4594
- Title: Subpoena Abuse Prevention Act
- Congress: 119
- Bill type: S
- Bill number: 4594
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-29T07:08:32Z
- Update date including text: 2026-05-29T07:08:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4594",
    "number": "4594",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Subpoena Abuse Prevention Act",
    "type": "S",
    "updateDate": "2026-05-29T07:08:32Z",
    "updateDateIncludingText": "2026-05-29T07:08:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T18:50:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4594is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4594\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Wyden (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 2703 of title 18, United States Code, to prohibit certain use of administrative subpoenas with respect to customer communications and records, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Subpoena Abuse Prevention Act .\n#### 2. Reforming subpoenas\n##### (a) Consistent protections for phone and app-Based call and texting records\nSection 2703(c)(2) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking subparagraph (C); and\n**(2)**\nby redesignating subparagraphs (D), (E), and (F) as subparagraphs (C), (D), and (E), respectively.\n##### (b) Prohibiting the use of subpoenas for bulk collection of certain subscriber information\nSection 2703(c)(2) of title 18, United States Code, as amended by subsection (a), is further amended in the matter following subparagraph (E), as so redesignated, by inserting , provided that for any administrative, grand jury, or trial subpoena, the governmental entity identifies the subscriber or customer by name, address, temporarily assigned network address, or account identifier (such as a username) before the period at the end.\n##### (c) Prohibiting the use of subpoenas with a purpose To investigate constitutionally protected activities\nSection 2703(c) of title 18, United States Code, is further amended by adding at the end the following:\n(4) Protections for constitutionally protected activities (A) In general A governmental entity may not use a subpoena to require the disclosures described in paragraph (2) if a purpose of the subpoena is to\u2014 (i) investigate, monitor, or otherwise acquire information about activities, or any person's engagement in activities, that are exercises of free speech, press, religion, assembly, or petition, or are otherwise protected by the Constitution of the United States; or (ii) retaliate against any person for their engagement in activities that are exercises of free speech, press, religion, assembly, or petition, or are otherwise protected by the Constitution of the United States. (B) Required certification (i) In general A governmental entity using a subpoena to require the disclosures described in paragraph (2) from a service provider shall provide a certification under penalty of perjury attesting that the subpoena is being made for a legitimate and lawful purpose, and not with a purpose described in subparagraph (A)\u2014 (I) to the service provider; and (II) when applying for a preclusion of notice order under section 2705(b), to the court in such application. (ii) Absence of certification A subpoena to require the disclosures described in paragraph (2) from a service provider shall not be valid, and a preclusion of notice order under section 2705(b) for such subpoena shall not issue, unless the subpoena includes the certification described in clause (i). .\n##### (d) Required disclosures\nSection 2703(c) of title 18, United States Code, is further amended by adding at the end the following:\n(5) Required disclosures to service provider (A) In general Except as provided in subparagraph (B)\u2014 (i) the service provider\u2014 (I) may notify a customer or subscriber of the receipt of the subpoena; and (II) may consult with an attorney in order to obtain legal advice or assistance regarding the subpoena; and (ii) the government entity shall inform the service provider that it\u2014 (I) is not being directed to not notify any other person of the existence of the subpoena; (II) may notify the customer or subscriber of the receipt of the subpoena; and (III) may consult with an attorney in order to obtain legal advice or assistance regarding the subpoena. (B) Exception for nondisclosure orders If a governmental entity described in subparagraph (A) obtains a preclusion of notice order under section 2705(b)\u2014 (i) such order may limit the right of the service provider described in subparagraph (A)(i)(I); and (ii) the governmental entity shall modify the required disclosures described in subclauses (I) and (II) of subparagraph (A)(ii) to be consistent with the terms of the order. .\n##### (e) Public reporting of use of administrative subpoenas\nSection 2703(c) of title 18, United States Code, is further amended by adding at the end the following:\n(6) Reporting of Federal use of administrative subpoenas Each Federal governmental entity that uses an administrative subpoena to require the disclosure of information under this subsection shall annually publicly publish a report containing, for the 1-year period preceding the date of the report\u2014 (A) the number of administrative subpoenas issued by the governmental entity, disaggregated by the statutory authority under which the administrative subpoenas were issued; and (B) the number of accounts for which the governmental entity received information through an administrative subpoena, disaggregated by the statutory authority under which the administrative subpoenas were issued. .",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4594is.xml"
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
      "title": "Subpoena Abuse Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:08:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Subpoena Abuse Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 2703 of title 18, United States Code, to prohibit certain use of administrative subpoenas with respect to customer communications and records, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:03:38Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8427?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8427
- Title: Congressional Pension Integrity Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8427
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-01T18:41:05Z
- Update date including text: 2026-05-01T18:41:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8427",
    "number": "8427",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Congressional Pension Integrity Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-01T18:41:05Z",
    "updateDateIncludingText": "2026-05-01T18:41:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-21T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "FL"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "VA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "CO"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "WA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8427ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8427\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mr. Subramanyam (for himself, Mrs. Luna , Mr. Walkinshaw , Ms. Boebert , Ms. Randall , and Ms. Mace ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend chapter 83 of title 5, United States Code, to prohibit pay of annuity or retired pay to a Member of Congress convicted of a criminal offense committed during congressional service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Congressional Pension Integrity Act of 2026 .\n#### 2. Pension eligibility for Members of Congress\n##### (a) In general\nSubchapter II of chapter 83 of title 5, United States Code, is amended by adding at the end the following:\n8323. Offenses committed by Members of Congress (a) An individual who is or was a Member of Congress, or the survivor or beneficiary of such individual, may not be paid annuity or retired pay on the basis of the service of the individual which is creditable toward the annuity or retired pay, if the individual was convicted of an offense named by subsection (b) of this section, to the extent provided by the paragraph, and the prohibition on payment of annuity or retired pay applies to the period after the earlier of\u2014 (1) the date of the conviction; or (2) if applicable, the date on which the status of the individual as a Member of Congress is terminated. (b) Each of the following is an offense to which subsection (a) of this section applies if the individual commits the offense, or begins committing the offense, while the individual is or was a Member of Congress: (1) Rape. (2) Sexual assault. (3) Sexual abuse of a minor. (4) Participation in a venture that causes another individual to engage in a sex act, on account of which anything of value is given to or received by any person, with the purpose of benefitting, whether financial or by receiving anything of value, from such participation. (5) A crime of violence, as such term is defined in section 16 of title 18. (6) An offense within the purview of\u2014 (A) chapter 11 (relating to bribery, graft, and conflict of interest), chapter 29 (relating to elections and political activities), chapter 31 (relating to embezzlement and theft), chapter 63 (relating to mail fraud and other fraud offenses), and chapter 73 (relating to obstruction of justice) of title 18; or (B) the Federal Election Campaign Act of 1971. (c) An individual who is or was a Member of Congress, or the survivor or beneficiary of such individual, may not be paid annuity or retired pay on the basis of the service of the individual which is creditable toward the annuity or retired pay, if the House of Congress with respect to which the individual is or was a Member of Congress determines, in accordance with the rules of the House of Congress, that the individual engaged in sexual conduct with another individual who was, at the time of the sexual conduct, an officer or employee in or of the House of Congress under the supervision of the individual, and the prohibition on payment of annuity or retired pay applies to the period after the earlier of\u2014 (1) the date of the determination; or (2) if applicable, the date on which the status of the individual as a Member of Congress is terminated. (d) This section shall take effect on the date on which the next succeeding Congress begins after the date of the enactment of this section and shall apply with respect to such dates of conviction, determination, and termination described in this section after the effective date. .\n##### (b) Conforming amendment\nThe table of sections for chapter 83 of title 5, United States Code, is amended by inserting after the item relating to section 8322 the following:\n8323. Offenses committed by Members of Congress. .",
      "versionDate": "2026-04-21",
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
        "name": "Congress",
        "updateDate": "2026-05-01T18:41:04Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8427ih.xml"
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
      "title": "Congressional Pension Integrity Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-25T04:38:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Pension Integrity Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-25T04:38:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 83 of title 5, United States Code, to prohibit pay of annuity or retired pay to a Member of Congress convicted of a criminal offense committed during congressional service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-25T04:33:32Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8300?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8300
- Title: Swalwell Act
- Congress: 119
- Bill type: HR
- Bill number: 8300
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-20T08:08:31Z
- Update date including text: 2026-05-20T08:08:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8300",
    "number": "8300",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Swalwell Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:31Z",
    "updateDateIncludingText": "2026-05-20T08:08:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:03:45Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "AZ"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "CO"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "GA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "FL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "FL"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "WI"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "PA"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NV"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "GA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8300ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8300\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Gosar (for himself, Mr. Biggs of Arizona , Ms. Boebert , Mr. Burchett , Mr. Carter of Georgia , Mr. Fine , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo prohibit the use of taxpayer funds for settlements of workplace misconduct claims involving Members of Congress or senior staff of the House of Representatives or the Senate, require personal financial accountability, ensure transparency of past settlements while protecting victims, and mandate referral of criminal allegations to the Department of Justice, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Wasteful Allowances for Lawmaker Wrongdoing and Ensuring Legal Liability Act or the Swalwell Act .\n#### 2. Prohibition on use of Federal funds in connection with workplace misconduct\n##### (a) In general\nNo funds appropriated or otherwise made available from the U.S. Treasury may be used to pay any settlement, award, or judgment arising from a claim of workplace misconduct by a Member of Congress or a senior staff of the House of Representatives or Senate.\n##### (b) Workplace misconduct defined\nFor purposes of this section, the term workplace misconduct includes claims of discrimination, harassment, retaliation, or other violations of employment or civil rights laws.\n#### 3. Personal liability of Members of Congress or a senior staff of the House of Representatives or Senate\n##### (a) In general\nAny Member of Congress or a senior staff of the House of Representatives or Senate found liable for, or entering into a settlement resolving, a workplace misconduct claim shall be personally responsible for the full amount of such settlement or award.\n##### (b) Prohibitions with respect to reimbursement\nNo Member of Congress or a senior staff of the House of Representatives or Senate may be reimbursed, directly or indirectly\u2014\n**(1)**\nwith Federal funds for any payment made under subsection (a) ; or\n**(2)**\nwith campaign funds for any payment made under subsection (a) .\n##### (c) Certification requirement\nMembers of Congress or a senior staff of the House of Representatives or Senate shall certify, under penalty of perjury, that no public funds were used in connection with such payments under subsection (a) .\n#### 4. Mandatory disclosure of settlements\n##### (a) In general\nThe Clerk of the House of Representatives and the Secretary of the Senate shall maintain and publish a publicly accessible, searchable database containing the following:\n**(1)**\nThe name of any Member of Congress or a senior staff of the House of Representatives or Senate who has settled or been found liable for a workplace misconduct claim.\n**(2)**\nThe total amount of any settlement or award.\n**(3)**\nThe date of resolution.\n**(4)**\nThe nature of the claim, described in general terms.\n##### (b) Prohibition\nThe database under subsection (a) shall not include any personally identifiable information of victims or complainants.\n##### (c) Disclosure deadline\nDisclosures shall be made not later than 30 days after the date of the resolution of a claim.\n#### 5. Retroactive disclosure of past settlements\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Clerk of the House and Secretary of the Senate shall publish all settlements and awards paid using public funds since January 1, 1995, relating to workplace misconduct claims involving Members of Congress or a senior staff of the House of Representatives or Senate.\n##### (b) Privacy protection requirement\nDisclosures under subsection (a) shall comply with the privacy protections set forth in section 4(b).\n#### 6. Referral of criminal allegations\n##### (a) In general\nAny allegation of conduct by a Member of Congress or a senior staff of the House of Representatives or Senate that may constitute a violation of Federal criminal law shall be promptly referred to the Department of Justice for review.\n##### (b) Source of referral\nA referral under subsection (a) shall be made by the Office of Congressional Workplace Rights, the Committee on Ethics of the House of Representatives, or the Select Committee on Ethics of the Senate, as applicable.\n##### (c) Restrictions on preventing or delaying referral\n**(1) In general**\nNo settlement agreement, nondisclosure agreement, or internal congressional process may prevent or delay a referral under subsection (a) .\n**(2) Other requirements**\nThe existence of a referral under this section shall not be contingent upon the consent of the complainant.\n#### 7. Enforcement and penalties\n##### (a) In general\nAny Member of Congress or a senior staff of the House of Representatives or Senate who violates this Act shall be subject to\u2014\n**(1)**\na civil penalty that equals not less than 200 percent of the amount improperly paid; and\n**(2)**\nreferral to the appropriate Ethics Committee for further disciplinary action.\n##### (b) Civil action\nThe Attorney General is authorized to bring a civil action to enforce compliance with this Act.\n#### 8. Definitions\nIn this Act\u2014\n**(1)**\nthe term Member of Congress includes a Delegate or Resident Commissioner to the Congress; and\n**(2)**\nthe term senior staff of the House of Representatives or Senate means any individual who, at the time a violation occurred, was required to file a report under subchapter I of chapter 131 of title 5, United States Code.\n#### 9. Rule of construction\nNothing in this Act may be construed to\u2014\n**(1)**\nlimit the rights of victims to pursue claims or receive compensation;\n**(2)**\nrequire the disclosure of a victim\u2019s identity, including sex and personally identifiable information, without their express written consent; or\n**(3)**\nprevent the House of Representatives or the Senate from taking such actions as may be necessary to protect the identities of victims.\n#### 10. Effective date\nThis Act shall take effect on the date of the enactment of this Act and shall apply to any claim pending on or after such date.",
      "versionDate": "2026-04-15",
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
        "updateDate": "2026-04-22T19:15:30Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8300ih.xml"
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
      "title": "Swalwell Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T09:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Swalwell Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Wasteful Allowances for Lawmaker Wrongdoing and Ensuring Legal Liability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of taxpayer funds for settlements of workplace misconduct claims involving Members of Congress or senior staff of the House of Representatives or the Senate, require personal financial accountability, ensure transparency of past settlements while protecting victims, and mandate referral of criminal allegations to the Department of Justice, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T09:19:01Z"
    }
  ]
}
```

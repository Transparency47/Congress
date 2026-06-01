# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/209
- Title: Protecting Minors from Medical Malpractice Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 209
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-12-05T21:47:41Z
- Update date including text: 2025-12-05T21:47:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/209",
    "number": "209",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Protecting Minors from Medical Malpractice Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:47:41Z",
    "updateDateIncludingText": "2025-12-05T21:47:41Z"
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
          "date": "2025-01-23T17:34:21Z",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s209is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 209\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Cotton (for himself, Mr. Banks , Mr. Sheehy , and Mr. Mullin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo protect children from medical malpractice in the form of gender-transition procedures.\n#### 1. Short title\nThis Act may be cited as the Protecting Minors from Medical Malpractice Act of 2025 .\n#### 2. Private right of action for a gender-transition procedure performed on a minor\n##### (a) In general\nA medical practitioner, in any circumstance described in subsection (c), who performs a gender-transition procedure on an individual who is less than 18 years of age shall, as described in subsection (b), be liable to the individual if injured (including any physical, psychological, emotional, or physiological harms) by such procedure, related treatment, or the aftereffects of the procedure or treatment.\n##### (b) Private right of action\nAn individual covered by subsection (a) who receives a gender-transition procedure from a medical practitioner (or a representative, including a legal guardian, on behalf of such individual) may, not later than the day that is 30 years after the date on which the individual turns 18 years of age, bring a civil action against such medical practitioner in a court of competent jurisdiction for\u2014\n**(1)**\ndeclaratory or injunctive relief;\n**(2)**\ncompensatory damages;\n**(3)**\npunitive damages; and\n**(4)**\nattorney\u2019s fees and costs.\n##### (c) Circumstances\nFor the purposes of subsection (a), the circumstances described in this subsection are that\u2014\n**(1)**\nthe medical practitioner or the individual receiving the gender-transition procedure traveled in interstate or foreign commerce, or traveled using a means, channel, facility, or instrumentality of interstate or foreign commerce, in furtherance of or in connection with the conduct described in subsection (a);\n**(2)**\nthe medical practitioner used a means, channel, facility, or instrumentality of interstate or foreign commerce in furtherance of or in connection with the conduct described in subsection (a);\n**(3)**\nany payment of any kind was made, directly or indirectly, in furtherance of or in connection with the conduct described in subsection (a) using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce;\n**(4)**\nthe medical practitioner transmitted in interstate or foreign commerce any communication relating to or in furtherance of the conduct described in subsection (a) using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce by any means or in any manner, including by computer, mail, wire, or electromagnetic transmission;\n**(5)**\nany instrument, item, substance, or other object that has traveled in interstate or foreign commerce was used to perform the conduct described in subsection (a);\n**(6)**\nthe conduct described in subsection (a) occurred within the special maritime and territorial jurisdiction of the United States, or any territory or possession of the United States; or\n**(7)**\nthe conduct described in subsection (a) otherwise occurred in or affected interstate or foreign commerce.\n#### 3. Preserving freedom of conscience and medical judgement for medical providers\nNotwithstanding any other provision of law, no provision of Federal law shall require, or be construed to require, a medical practitioner to perform a gender-transition procedure.\n#### 4. Prohibition on funding for certain States\nNotwithstanding any other provision of law, any State that requires medical practitioners to perform any gender-transition procedure on an individual in the State shall be ineligible to receive any Federal funding from the Department of Health and Human Services.\n#### 5. Definitions\nIn this Act:\n**(1) Biological sex**\nThe term biological sex means the genetic classification of an individual as male or female, as reflected in the organization of the body of such individual for a reproductive role or capacity, such as through sex chromosomes, naturally occurring sex hormones, and internal and external genitalia present at birth, without regard to the subjective sense of identity of the individual.\n**(2) Gender-transition procedure**\n**(A) In general**\nExcept as provided in subparagraph (B), the term gender-transition procedure means\u2014\n**(i)**\nthe prescription or administration of puberty-blocking drugs for the purpose of changing the body of an individual so that it conforms to the subjective sense of identity of the individual, in the case such identity is at odds with the individual's biological sex;\n**(ii)**\nthe prescription or administration of cross-sex hormones for the purpose of changing the body of an individual so that it conforms to the subjective sense of identity of the individual, in the case such identity is at odds with the individual\u2019s biological sex; or\n**(iii)**\na surgery to change the body of an individual so that it conforms to the subjective sense of identity of the individual, in the case such identity is at odds with the individual\u2019s biological sex.\n**(B) Exception**\nThe term gender-transition procedure does not include\u2014\n**(i)**\nan intervention described in subparagraph (A) that is performed on\u2014\n**(I)**\nan individual with biological sex characteristics that are inherently ambiguous, such as those born with 46 XX chromosomes with virilization, 46 XY chromosomes with undervirilization, or having both ovarian and testicular tissue; or\n**(II)**\nan individual with respect to whom a physician has determined through genetic or biochemical testing that the individual does not have normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action, for a biological male or biological female;\n**(ii)**\nthe treatment of any infection, injury, disease, or disorder that has been caused or exacerbated by the performance of an intervention described in subparagraph (A) without regard to whether the intervention was performed in accordance with State or Federal law or whether the intervention is covered by the private right of action under section 2; or\n**(iii)**\nany procedure undertaken because the individual suffers from a physical disorder, physical injury, or physical illness that would, as certified by a physician, place the individual in imminent danger of death or impairment of major bodily function unless the procedure is performed.\n**(3) Medical practitioner**\nThe term medical practitioner means a person who is licensed, certified, or otherwise authorized by the laws of a State to administer health care in the ordinary course of the practice of the person\u2019s profession.\n#### 6. Effective date\nThis Act shall take effect on the date of enactment of this Act.",
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
        "actionDate": "2025-01-23",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on the Judiciary, Education and Workforce, Natural Resources, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "653",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Minors from Medical Malpractice Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child health",
            "updateDate": "2025-03-17T16:12:54Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-17T16:12:54Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-03-17T16:12:54Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-17T16:12:54Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-17T16:12:54Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-03-17T16:12:54Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-17T16:12:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T14:33:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s209",
          "measure-number": "209",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s209v00",
            "update-date": "2025-04-15"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Minors from Medical Malpractice Act of 2025</strong></p><p>This bill makes a medical practitioner who performs a gender-transition procedure on an individual who is less than 18 years of age liable for any physical, psychological, emotional, or physiological harms from the procedure for 30 years after the individual turns 18.</p><p>Additionally, if a state requires medical practitioners to perform gender-transition procedures, that state shall be ineligible for federal funding from the Department of Health and Human Services.</p><p>Under the bill, <em>g</em><em>ender-transition procedures</em> generally include certain surgeries or hormone therapies that change the body of an individual to correspond to a sex that is discordant with the individual's biological sex. They exclude, however, interventions to treat (1) individuals who either have ambiguous external biological sex characteristics or lack a normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action; (2) infections, injuries, diseases, or disorders caused by a gender-transition procedure; or (3) a physical disorder, injury, or illness that places an individual in imminent danger of death or impairment of a major bodily function.</p>"
        },
        "title": "Protecting Minors from Medical Malpractice Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s209.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Minors from Medical Malpractice Act of 2025</strong></p><p>This bill makes a medical practitioner who performs a gender-transition procedure on an individual who is less than 18 years of age liable for any physical, psychological, emotional, or physiological harms from the procedure for 30 years after the individual turns 18.</p><p>Additionally, if a state requires medical practitioners to perform gender-transition procedures, that state shall be ineligible for federal funding from the Department of Health and Human Services.</p><p>Under the bill, <em>g</em><em>ender-transition procedures</em> generally include certain surgeries or hormone therapies that change the body of an individual to correspond to a sex that is discordant with the individual's biological sex. They exclude, however, interventions to treat (1) individuals who either have ambiguous external biological sex characteristics or lack a normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action; (2) infections, injuries, diseases, or disorders caused by a gender-transition procedure; or (3) a physical disorder, injury, or illness that places an individual in imminent danger of death or impairment of a major bodily function.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119s209"
    },
    "title": "Protecting Minors from Medical Malpractice Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Minors from Medical Malpractice Act of 2025</strong></p><p>This bill makes a medical practitioner who performs a gender-transition procedure on an individual who is less than 18 years of age liable for any physical, psychological, emotional, or physiological harms from the procedure for 30 years after the individual turns 18.</p><p>Additionally, if a state requires medical practitioners to perform gender-transition procedures, that state shall be ineligible for federal funding from the Department of Health and Human Services.</p><p>Under the bill, <em>g</em><em>ender-transition procedures</em> generally include certain surgeries or hormone therapies that change the body of an individual to correspond to a sex that is discordant with the individual's biological sex. They exclude, however, interventions to treat (1) individuals who either have ambiguous external biological sex characteristics or lack a normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action; (2) infections, injuries, diseases, or disorders caused by a gender-transition procedure; or (3) a physical disorder, injury, or illness that places an individual in imminent danger of death or impairment of a major bodily function.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119s209"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s209is.xml"
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
      "title": "Protecting Minors from Medical Malpractice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Minors from Medical Malpractice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect children from medical malpractice in the form of gender-transition procedures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:22Z"
    }
  ]
}
```

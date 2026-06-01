# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6334?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6334
- Title: Deepfake Liability Act
- Congress: 119
- Bill type: HR
- Bill number: 6334
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2025-12-10T17:47:46Z
- Update date including text: 2025-12-10T17:47:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6334",
    "number": "6334",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "A000148",
        "district": "4",
        "firstName": "Jake",
        "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
        "lastName": "Auchincloss",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Deepfake Liability Act",
    "type": "HR",
    "updateDate": "2025-12-10T17:47:46Z",
    "updateDateIncludingText": "2025-12-10T17:47:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T17:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6334ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6334\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Auchincloss (for himself and Ms. Maloy ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend section 230 of the Communications Act of 1934 and the TAKE IT DOWN Act to combat cyberstalking and intimate privacy violations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deepfake Liability Act .\n#### 2. Amendments to section 230 of Communications Act of 1934\n##### (a) Duty of care\nSection 230(c)(1) of the Communications Act of 1934 ( 47 U.S.C. 230(c)(1) ) is amended\u2014\n**(1)**\nby striking No provider and inserting the following:\n(A) In general Except as provided in subparagraph (B), no provider ; and\n**(2)**\nby adding at the end the following:\n(B) Cyberstalking and intimate privacy violations (i) Duty of care Subparagraph (A) only applies to a provider of an interactive computer service if such provider is implementing, with respect to the interactive computer service of the provider, a reasonable process for addressing cyberstalking and intimate privacy violations that includes, at a minimum, the following: (I) A process to prevent, to the extent practicable, cyberstalking and intimate privacy violations. (II) A clear and accessible process to implement section 3(a) of the TAKE IT DOWN Act ( 47 U.S.C. 223a(a) ) (relating to notice and removal of intimate privacy violations and content relating to cyberstalking). (III) Minimum data logging requirements that\u2014 (aa) preserve data necessary for legal proceedings related to cyberstalking or an intimate privacy violation; and (bb) ensure that preserved data is not transferred or otherwise used for a purpose other than a legal proceeding related to cyberstalking or an intimate privacy violation. (IV) A process to remove or block content that has been determined unlawful by a court. (V) Any other process or requirement determined necessary by the Commission to address cyberstalking and intimate privacy violations. (ii) Definitions In this subparagraph: (I) Consent The term consent has the meaning given such term in section 223(h)(1). (II) Cyberstalking The term cyberstalking means a deliberate course of conduct\u2014 (aa) directed at a specific individual; (bb) that causes the individual to suffer substantial emotional distress or the fear of bodily harm; and (cc) that would cause a reasonable individual to suffer substantial emotional distress or the fear of bodily harm. (III) Intimate privacy violation The term intimate privacy violation means the following: (aa) An intimate visual depiction obtained or shared without the consent of an individual portrayed in the depiction. (bb) A sexually explicit digital forgery made or shared without the consent of an individual portrayed in the sexually explicit digital forgery. (IV) Intimate visual depiction The term intimate visual depiction has the meaning given such term in section 1309(a) of division W of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851(a) ). (V) Sexually explicit digital forgery The term sexually explicit digital forgery has the meaning given such term in section 223(h)(1). .\n##### (b) Information content provider defined\nSection 230(f)(3) of the Communications Act of 1934 ( 47 U.S.C. 230(f)(3) ) is amended by striking creation or development and inserting creation or development (including through solicitation, encouragement, or the use of a generative model) .\n#### 3. Amendments to TAKE IT DOWN Act\n##### (a) Criminal prohibitions\n**(1) Sexually explicit digital forgeries**\nSection 223(h) of the Communications Act of 1934 ( 47 U.S.C. 223(h) ) is amended\u2014\n**(A)**\nin paragraph (1), by amending subparagraph (B) to read as follows:\n(B) Sexually explicit digital forgery The term sexually explicit digital forgery means an intimate visual depiction of an identifiable individual that has been created, materially manipulated, altered, or annotated so that such depiction is virtually indistinguishable from an authentic visual depiction of such individual. ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin the heading, by striking digital forgeries and inserting sexually explicit digital forgeries ; and\n**(ii)**\nby striking digital forgery each place it appears and inserting sexually explicit digital forgery ; and\n**(C)**\nin paragraph (6)(B), in the heading, by striking digital forgeries and inserting sexually explicit digital forgeries .\n**(2) Elimination of certain exceptions**\nSection 223(h) of the Communications Act of 1934 ( 47 U.S.C. 223(h) ), as amended by the preceding provisions of this Act, is further amended\u2014\n**(A)**\nin paragraph (2)(C)\u2014\n**(i)**\nin clause (iii), by striking the semicolon and inserting ; or ;\n**(ii)**\nby striking clause (iv); and\n**(iii)**\nby redesignating clause (v) as clause (iv); and\n**(B)**\nin paragraph (3)(C)\u2014\n**(i)**\nin clause (iii), by striking the semicolon and inserting ; or ;\n**(ii)**\nby striking clause (iv); and\n**(iii)**\nby redesignating clause (v) as clause (iv).\n##### (b) Notice and removal process\n**(1) In general**\nSection 3 of the TAKE IT DOWN Act ( 47 U.S.C. 223a ) is amended\u2014\n**(A)**\nin the heading, by striking nonconsensual intimate visual depictions and inserting intimate privacy violations and content relating to cyberstalking ;\n**(B)**\nby amending subsection (a) to read as follows:\n(a) In general (1) Notice and removal process (A) Establishment A covered platform shall establish a process whereby a covered individual (or an authorized person acting on behalf of such individual) may\u2014 (i) notify the covered platform of\u2014 (I) an intimate privacy violation or content relating to cyberstalking published on the covered platform\u2014 (aa) that includes a depiction of the covered individual; (bb) that was published without the consent of the covered individual; (cc) that depicts matter that was not voluntarily exposed by the covered individual in a public or commercial setting; (dd) that does not depict a matter of public concern; and (ee) publication of which\u2014 (AA) causes the covered individual to suffer substantial emotional distress or the fear of bodily harm; and (BB) would cause a reasonable individual to suffer substantial emotional distress or the fear of bodily harm; or (II) content relating to cyberstalking published on the covered platform\u2014 (aa) that is directed at the covered individual; (bb) that was published without the consent of the covered individual; (cc) that does not refer to a matter of public concern; and (dd) publication of which\u2014 (AA) causes the covered individual to suffer substantial emotional distress or the fear of bodily harm; and (BB) would cause a reasonable individual to suffer substantial emotional distress or the fear of bodily harm; and (ii) submit a request for the covered platform to remove such intimate privacy violation or content relating to cyberstalking. (B) Requirements A notification and request for removal of an intimate privacy violation or content relating to cyberstalking submitted under the process established under subparagraph (A) shall include, in writing\u2014 (i) a physical or electronic signature of the covered individual (or an authorized person acting on behalf of such individual); (ii) an identification of, and information reasonably sufficient for the covered platform to locate, the intimate privacy violation or content relating to cyberstalking; (iii) a brief statement that the covered individual has a good faith belief that the intimate privacy violation or content relating to cyberstalking was published without the consent of the covered individual, including any relevant information for the covered platform to determine that the intimate privacy violation or content relating to cyberstalking was published without the consent of the covered individual; (iv) information sufficient to enable the covered platform to contact the covered individual (or an authorized person acting on behalf of such individual); and (v) a statement that the information in the notification and request for removal is accurate, and, under penalty of perjury, that the party submitting the notification and request for removal is the covered individual depicted in the intimate privacy violation or content relating to cyberstalking or the covered individual at whom the content relating to cyberstalking is directed (or an authorized person acting on behalf of such individual). (2) Notice of process A covered platform shall provide on the platform a clear and conspicuous notice, which may be provided through a clear and conspicuous link to another web page or disclosure, of the notice and removal process established under paragraph (1)(A) that\u2014 (A) is easy to read and in plain language; and (B) provides information regarding the responsibilities of the covered platform under this section, including a description of how an individual can submit a notification and request for removal. (3) Removal of intimate privacy violations and content relating to cyberstalking Upon receiving a valid removal request from a covered individual (or an authorized person acting on behalf of such individual) using the process described in paragraph (1)(A)(ii), a covered platform shall, as soon as possible, but not later than 48 hours after receiving such request\u2014 (A) remove the intimate privacy violation or content relating to cyberstalking; and (B) make reasonable efforts to identify and remove any known identical copies of the intimate privacy violation or content relating to cyberstalking. (4) Limitation on liability A covered platform shall not be liable for any claim based on the covered platform\u2019s good faith disabling of access to, or removal of, material claimed to be a nonconsensual intimate privacy violation or nonconsensual content relating to cyberstalking based on facts or circumstances from which the unlawful publishing of an intimate privacy violation or content relating to cyberstalking is apparent, regardless of whether the intimate privacy violation or content relating to cyberstalking is ultimately determined to be unlawful or not. ; and\n**(C)**\nin subsection (b)(2)\u2014\n**(i)**\nin subparagraph (A), by striking Except as provided in subparagraph (D), the and inserting The ; and\n**(ii)**\nby striking subparagraph (D).\n**(2) Definitions**\nSection 4 of the TAKE IT DOWN Act ( 47 U.S.C. 223a note) is amended by striking paragraphs (2) and (3) and inserting the following:\n(2) Consent The term consent has the meaning given such term in section 223(h)(1) of the Communications Act of 1934 ( 47 U.S.C. 223(h)(1) ). (3) Covered individual The term covered individual means\u2014 (A) an individual\u2014 (i) who appears in whole or in part in an intimate privacy violation or content relating to cyberstalking; and (ii) whose face, likeness, or other distinguishing characteristic (including a unique birthmark or other recognizable feature) is displayed in connection with such intimate privacy violation or content relating to cyberstalking; and (B) a specific individual at whom content relating to cyberstalking is directed. (4) Covered platform (A) In general The term covered platform means a website, online service, online application, or mobile application that is accessible to the public. (B) Exclusions The term covered platform does not include the following: (i) A provider of broadband internet access service (as described in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation). (ii) Electronic mail. (iii) A messaging service. (iv) A data storage service. (5) Cyberstalking The term cyberstalking has the meaning given such term in section 230(c)(1)(B)(ii) of the Communications Act of 1934 ( 47 U.S.C. 230(c)(1)(B)(ii) ). (6) Intimate privacy violation The term intimate privacy violation has the meaning given such term in section 230(c)(1)(B)(ii) of the Communications Act of 1934 ( 47 U.S.C. 230(c)(1)(B)(ii) ). .\n#### 4. General provisions\n##### (a) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Federal Trade Commission, in consultation with the Federal Communications Commission and (as appropriate) with the Attorney General, shall promulgate regulations under section 553 of title 5, United States Code, to implement the amendments made by this Act.\n##### (b) Applicability\nThe amendments made by this Act shall apply to information made available on an interactive computer service (as defined in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) )) or a covered platform (as defined in section 4 of the TAKE IT DOWN Act ( 47 U.S.C. 223a note), as amended by this Act) on or after the date of the enactment of this Act.\n##### (c) Rule of construction\nThe amendments made by this Act may not be construed to infringe upon any right protected under the First Amendment to the Constitution.",
      "versionDate": "2025-12-01",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-10T17:47:46Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6334ih.xml"
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
      "title": "Deepfake Liability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deepfake Liability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 230 of the Communications Act of 1934 and the TAKE IT DOWN Act to combat cyberstalking and intimate privacy violations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:25Z"
    }
  ]
}
```

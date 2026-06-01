# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1466
- Title: Cardiac Arrest Survival Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1466
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-11-18T09:05:37Z
- Update date including text: 2025-11-18T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1466",
    "number": "1466",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000472",
        "district": "18",
        "firstName": "Scott",
        "fullName": "Rep. Franklin, Scott [R-FL-18]",
        "lastName": "Franklin",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Cardiac Arrest Survival Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:37Z",
    "updateDateIncludingText": "2025-11-18T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:37:15Z",
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
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "VA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "VA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1466ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1466\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Scott Franklin of Florida (for himself, Mr. Connolly , Mr. Bilirakis , Mr. Soto , Mrs. Cammack , Mr. Calvert , Mr. Van Drew , Mr. Cline , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to clarify liability protections regarding emergency use of automated external defibrillators.\n#### 1. Short title\nThis Act may be cited as the Cardiac Arrest Survival Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEstablishing a nationally uniform baseline of protection from civil liability for persons who use automated external defibrillators (in this section referred to as AEDs ) in perceived medical emergencies, who own or hold other property interests in AEDs used in perceived medical emergencies, or who own, occupy, or manage premises in which an AED is used or from which an AED is taken for use in a perceived medical emergency will encourage the deployment of additional AEDs, which will ultimately save lives that would otherwise have been lost to cardiac arrest.\n**(2)**\nThe current patchwork of State Good Samaritan laws provides incomplete, inconsistent, and, in some instances, inadequate protection for entities considering the acquisition or deployment of AEDs. In these circumstances, concerns about potential liability resulting from the good-faith acquisition and deployment of this life-saving technology are inhibiting its deployment.\n**(3)**\nSuch concerns are especially acute for entities with operations or facilities in multiple States, yet such entities are also among those in which the widespread deployment of AEDs would be most beneficial.\n**(4)**\nA nationally uniform baseline of protection from civil liability is needed for persons who use AEDs in perceived medical emergencies, who own or hold other property interests in AEDs used in perceived medical emergencies, or who own, occupy, or manage premises in which an AED is used or from which an AED is taken for use in a perceived medical emergency.\n#### 3. Liability regarding emergency use of automated external defibrillators\nSection 248 of the Public Health Service Act ( 42 U.S.C. 238q ) is amended to read as follows:\n248. Liability regarding emergency use of automated external defibrillators (a) Good samaritan protections (1) In general Except as provided in subsection (e), a person described in paragraph (2) is immune from civil liability for any harm resulting from the use or attempted use of an automated external defibrillator device (in this section referred to as an AED ). (2) Good Samaritan described A person described in this paragraph is a person who\u2014 (A) uses or attempts to use an AED on a victim of a perceived medical emergency, and (B) is not the owner-acquirer (as defined in subsection (c)(2)) of the AED. (b) Premises owner/Lessee/Manager protections (1) In general Except as provided in subsection (e), a person described in paragraph (2) is immune from civil liability for any harm resulting from such use or attempted use of an AED. (2) Premises owner/lessee/manager described A person described in this paragraph is a person who\u2014 (A) owns, occupies under a lease or similar arrangement, or manages\u2014 (i) the premises at which an AED is used or attempted to be used on a victim of a perceived medical emergency, or (ii) the premises from which an AED used or attempted to be used on a victim of a perceived medical emergency is taken for such use, and (B) is not the owner-acquirer of such AED. (c) Device owner-Acquirer protections (1) In general Except as provided in subsection (e), an owner-acquirer of an AED is immune from civil liability for any harm resulting from the use or attempted use of such AED, unless the harm was proximately caused by the failure of the owner-acquirer to properly maintain the AED according to the guidelines of the manufacturer of the AED. (2) Owner-acquirer defined For purposes of this section, the term owner-acquirer means any person who owns or has otherwise acquired a possessory property interest in an AED that is used or attempted to be used on a victim of a perceived medical emergency. (d) Applicability of immunity in certain circumstances The immunity provided by subsections (a), (b), and (c) of this section shall apply regardless of whether\u2014 (1) the AED that is used or attempted to be used is marked with, or accompanied by, cautionary signage; (2) the AED that is used or attempted to be used is registered with any government; (3) the person who used or attempted to use the AED saw, read, understood, complied with, or attempted to comply with any cautionary signage present; (4) the person who used or attempted to use the AED had received any training relating to the use of\u2014 (A) AEDs in general; or (B) the particular AED used or attempted to be used; or (5) the person who used or attempted to use the AED was assisted or supervised by any other person, including a licensed physician. (e) Inapplicability of immunity in certain circumstances Notwithstanding subsection (d), immunity under subsection (a), (b), or (c)(1) does not apply to a person if\u2014 (1) such person\u2019s willful or criminal misconduct, gross negligence, reckless misconduct, or a conscious, flagrant indifference to the rights or safety of the victim proximately caused the harm involved; (2) such person is a licensed or certified health professional who used the AED while acting within the scope of the license or certification of the professional and within the scope of the employment or agency of the professional; (3) such person is a hospital, clinic, or other entity whose purpose is providing health care directly to patients, and the harm was caused by an employee or agent of the entity who used the AED while acting within the scope of the employment or agency of the employee or agent; or (4) such person is an owner-acquirer of the AED who leased the AED to a health care entity (or who otherwise provided the AED to such entity for compensation without selling the AED to the entity), and the harm was caused by an employee or agent of the entity who used the AED while acting within the scope of the employment or agency of the employee or agent. (f) Rules of construction (1) In general The following apply with respect to this section: (A) This section does not establish any cause of action, or require that an AED be placed at any building or other location. (B) With respect to the class of persons for which this section provides immunity from civil liability, this section preempts the law of any State to the extent that the otherwise-applicable State law would allow for civil liability in any circumstance where this section would provide immunity from civil liability. (C) This section does not waive any protection from liability for Federal officers or employees under\u2014 (i) section 233 of this title; or (ii) sections 1346(b), 2672, and 2679 of title 28, United States Code, or under alternative benefits provided by the United States where the availability of such benefits precludes a remedy under section 1346(b) of such title 28. (2) Civil actions under federal law (A) In general The applicability of subsections (a), (b), (c), (d), and (e) includes applicability to any action for civil liability described in subsection (a), (b), or (c) that arises under Federal law. (B) Federal areas adopting State law If a geographic area is under Federal jurisdiction and is located within a State but out of the jurisdiction of the State, and if, pursuant to Federal law, the law of the State applies in such area regarding matters for which there is no applicable Federal law, then an action for civil liability described in subsection (a), (b), or (c) that in such area arises under the law of the State is subject to subsections (a) through (f) in lieu of any related State law that would apply in such area in the absence of this subparagraph. (g) Federal jurisdiction (1) In any civil action arising under State law, the courts of the State involved have jurisdiction to apply the provisions of this section. (2) The actual, asserted, or potential application of any provision of this section in any civil action or as to any civil claim shall not establish the original jurisdiction of the Federal courts over such action or claim under section 1331 of title 28, United States Code. (h) Definitions (1) Perceived medical emergency For purposes of this section, the term perceived medical emergency means circumstances in which the behavior of an individual leads a reasonable person to believe that the individual is experiencing a life-threatening medical condition that requires an immediate medical response regarding the heart or other cardiopulmonary functioning of the individual. (2) Other definitions For purposes of this section: (A) The term automated external defibrillator device or AED means a defibrillator device that\u2014 (i) is commercially distributed in accordance with the Federal Food, Drug, and Cosmetic Act; (ii) is capable of recognizing the presence or absence of ventricular fibrillation, and is capable of determining without intervention by the user of the device whether defibrillation should be performed; (iii) upon determining that defibrillation should be performed, is able to deliver an electrical shock to an individual; and (iv) in the case of a defibrillator device that may be operated in either an automated or a manual mode, is set to operate in the automated mode. (B) The term cautionary signage means, with respect to an AED, any verbal or non-verbal markings or language purporting to limit use of the AED by members of the general public or to permit use of the AED only by persons with specific skills, qualifications, or training. (C) (i) The term harm includes physical, nonphysical, economic, and noneconomic losses. (ii) The term economic loss means any pecuniary loss resulting from harm (including the loss of earnings or other benefits related to employment, medical expense loss, replacement services loss, loss due to death, burial costs, and loss of business or employment opportunities) to the extent recovery for such loss is allowed under applicable State law. (iii) The term noneconomic losses means losses for physical and emotional pain, suffering, inconvenience, physical impairment, mental anguish, disfigurement, loss of enjoyment of life, loss of society and companionship, loss of consortium (other than loss of domestic service), hedonic damages, injury to reputation and all other nonpecuniary losses of any kind or nature. .",
      "versionDate": "2025-02-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-07-14T15:25:35Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-07-14T15:25:35Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-07-14T15:25:35Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-07-14T15:25:35Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-07-14T15:25:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T12:46:49Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1466ih.xml"
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
      "title": "Cardiac Arrest Survival Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cardiac Arrest Survival Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to clarify liability protections regarding emergency use of automated external defibrillators.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:21Z"
    }
  ]
}
```
